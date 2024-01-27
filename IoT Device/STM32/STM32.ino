//--------------------------------------------IMPORTING LIBRARIES------------------------------------------------------------------------------------------------------//

#include <Arduino.h>
#include <SoftwareSerial.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include "AESLib.h"
#include "Seeed_mbedtls.h"

//--------------------------------------------IMPORTING LIBRARIES------------------------------------------------------------------------------------------------------//



//--------------------------------------------ENCRYPTION VARIABLES----------------------------------------------------------------------------------------------------------//

String plaintext = "HELLO WORLD!";
String padding = "                ";
String payload;
String encrypted;

char cleartext[256];
char ciphertext[512];

// AES Encryption Key
byte aes_key[] = { 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30 };

// General initialization vector (you must use your own IV's in production for full security!!!)
byte aes_iv[N_BLOCK] = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };

unsigned long loopcount = 0;
byte enc_iv[N_BLOCK] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }; // iv_block gets written to, provide own fresh copy...
byte dec_iv[N_BLOCK] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

//--------------------------------------------ENCRYPTION VARIABLES----------------------------------------------------------------------------------------------------------//



//----------------------------------------------HASHING VARIABLES----------------------------------------------------------------------------------------------------------//

char *key = "secretKey";
byte hmacResult[32];

//----------------------------------------------HASHING VARIABLES----------------------------------------------------------------------------------------------------------//



//-----------------------------------------------I/O VARIABLES----------------------------------------------------------------------------------------------------------//

const int analogInPin1 = A0;
const int analogInPin2 = A3;
const int buzz = 4;
const int SENSOR1 = 8;
const int SENSOR2 = 9;
int sensorValue1 = 0;
int sensorValue2 = 0;
float sensorr1 ;
float sensorr2 ;  

//-----------------------------------------------I/O VARIABLES----------------------------------------------------------------------------------------------------------//



//--------------------------------------------OBJECT INITIALIZATION------------------------------------------------------------------------------------------------------//

// Initializing the esp8266 Object using Software Serial Class
SoftwareSerial esp8266(2, 3); // RX, TX pins on STM32F446RE (you can use any available pins)

// Initializing the AESLib Object using AESLib Class
AESLib aesLib;

// Initialising the OneWire Objects
OneWire oneWire1(SENSOR1);
OneWire oneWire2(SENSOR2);

// Initialising the DallasTemperature objects with OneWire Objects
DallasTemperature Temp1(&oneWire1);
DallasTemperature Temp2(&oneWire2);  

//--------------------------------------------OBJECT INITIALIZATION------------------------------------------------------------------------------------------------------//



//--------------------------------------------FUNCTION DECLARATIONS------------------------------------------------------------------------------------------------------//

// AES-256 Encryption Function
String encrypt_impl(char * msg, byte iv[]) {
  int msgLen = strlen(msg);
  char encrypted[2 * msgLen] = {0};
  aesLib.encrypt64((const byte*)msg, msgLen, encrypted, aes_key, sizeof(aes_key), iv);
  return String(encrypted);
}

// Generate IV (once)
void aes_init() {
  Serial.println("gen_iv()");
  aesLib.gen_iv(aes_iv);
  Serial.println("encrypt_impl()");
  Serial.println(encrypt_impl(strdup(plaintext.c_str()), aes_iv));
}

void TransmitJson(String method, String route, String encrypted, String hashop){

  payload = encrypted+","+hashop+","+method+","+route+",";

//  String ESPPost = String(method)+" "+String(route)+" HTTP/1.1\r\nHost: 192.168.0.106\r\nContent-Type: application/json\r\nContent-Length:"+String(payload.length())+"\r\n\r\n"+String(payload)+"\r\n";
//  String ESPSendLength = "AT+CIPSEND="+String(ESPPost.length())+"\r\n";

  // TCP Transmission

  esp8266.println(payload);

  delay(5000);
   
}

//--------------------------------------------FUNCTION DECLARATIONS------------------------------------------------------------------------------------------------------//



//-----------------------------------------------SETUP FUNCTION----------------------------------------------------------------------------------------------------------//

void setup() {
  // Begin Serial Communication
  Serial.begin(115200);

  // Begin esp8266 Communication
  esp8266.begin(115200);

  // Initializing the sensors
  Temp1.begin();
  Temp2.begin();

  pinMode(buzz, OUTPUT);

  aes_init();
  aesLib.set_paddingmode(paddingMode::CMS);

  // Initializing the Encryption Prerequisites
  char b64in[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

  char b64out[base64_enc_len(sizeof(aes_iv))];
  base64_encode(b64out, b64in, 16);

  char b64enc[base64_enc_len(10)];
  base64_encode(b64enc, (char*) "0123456789", 10);

  char b64dec[ base64_dec_len(b64enc, sizeof(b64enc))];
  base64_decode(b64dec, b64enc, sizeof(b64enc));
 
}

//-----------------------------------------------SETUP FUNCTION----------------------------------------------------------------------------------------------------------//



//-----------------------------------------------LOOP FUNCTION-----------------------------------------------------------------------------------------------------------//

void loop() {

  sensorValue1 = analogRead(analogInPin1);
//  sensorValue2 = analogRead(analogInPin2);
 
  Serial.print("sensorValue1: ");
  Serial.println(sensorValue1);
 
//  Serial.print("sensorValue2: ");
//  Serial.println(sensorValue2);
 
  if (sensorValue1 > 975){
    digitalWrite(buzz, LOW);
 

  // Sensor Readings Begin

  // Initiating a temperature conversion process in a DallasTemperature sensor
  Temp1.requestTemperatures();
  Temp2.requestTemperatures();

  // Storing the values into float variables using getTempCByIndex() method
  sensorr1 = Temp1.getTempCByIndex(0);
  sensorr2 = Temp2.getTempCByIndex(0);

  String Data = "{\"Device_Id\": \"1\", \"Status\": \"Working\", \"Temperature1\": " + String(sensorr1) + ", \"Temperature2\": " + String(sensorr2) + ", \"Date\": \"24-01-27\", \"Time\": \"00:00:00\"}";
  Serial.println(Data);
  // Sensor Readings End

 

  // Data Encryption Begin
 
  String readBuffer = padding + Data;
  Serial.println("INPUT:" + readBuffer);

  sprintf(cleartext, "%s", readBuffer.c_str()); // must not exceed 255 bytes; may contain a newline

  // Encryption
  encrypted = encrypt_impl(cleartext, enc_iv);
  sprintf(ciphertext, "%s", encrypted.c_str());
  Serial.print("Ciphertext: ");
  Serial.println(encrypted);
  delay(1000);
  for (int i = 0; i < 16; i++) {
    enc_iv[i] = 0;
    dec_iv[i] = 0;
  }

  // Data Encryption End


  // Data Hashing Begin

  const char *hashpay  = Data.c_str();

  mbedtls_md_context_t ctx;
  mbedtls_md_type_t md_type = MBEDTLS_MD_SHA256;
 
  const size_t payloadLength = strlen(hashpay);
  const size_t keyLength = strlen(key);            
 
  mbedtls_md_init(&ctx);
  mbedtls_md_setup(&ctx, mbedtls_md_info_from_type(md_type), 1);
  mbedtls_md_hmac_starts(&ctx, (const unsigned char *) key, keyLength);
  mbedtls_md_hmac_update(&ctx, (const unsigned char *) hashpay, payloadLength);
  mbedtls_md_hmac_finish(&ctx, hmacResult);
  mbedtls_md_free(&ctx);

  Serial.print("Hash: ");
  String hashop = "";
 
  for(int i= 0; i< sizeof(hmacResult); i++){
      char str[3];
      sprintf(str, "%02x", (int)hmacResult[i]);
      hashop += str;
      Serial.print(str);
  }
 
  // Data Hashing Begin


 
  // Encrypted Payload Transmission Begin
 
  TransmitJson("POST", "/decode", encrypted, hashop);
 
  // Encrypted Payload Transmission End



  // Status Printing on Serial terminal Begin
 
  if (esp8266.available()) {
    char c = esp8266.read();
    Serial.write(c);
  }

  if (Serial.available()) {
    char c = Serial.read();
    esp8266.write(c);
  }
  }
 
    digitalWrite(buzz, HIGH);
 

  // Status Printing on Serial terminal End
}

//-----------------------------------------------LOOP FUNCTION-----------------------------------------------------------------------------------------------------------//