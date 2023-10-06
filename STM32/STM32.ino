//--------------------------------------------IMPORTING LIBRARIES------------------------------------------------------------------------------------------------------//

#include <Arduino.h>
#include <SoftwareSerial.h>
#include "AESLib.h"

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



//-----------------------------------------------WIFI VARIABLES----------------------------------------------------------------------------------------------------------//

// SSID PASSWORD
String WifiSSID = "Manjrekar";
String WifiPSWD = "15atharva07";

// SERVER DATA
String IP = "192.168.0.106";
int Port = 8081;

// AT COMMANDS LIST
String Data;
String ESPReset = "AT+RST";
String ESPAT = "AT";
String ESPChangeMode = "AT+CWMODE=1";
String ESPGetWifi = "AT+CWJAP=\""+String(WifiSSID)+"\",\""+String(WifiPSWD)+"\"\r\n";
String ESPBeginTransmission = "AT+CIPSTART=\"TCP\",\""+String(IP)+"\","+String(Port)+"\r\n";
String ESPEndTransmission = "AT+CIPCLOSE\r\n";

//-----------------------------------------------WIFI VARIABLES----------------------------------------------------------------------------------------------------------//


//--------------------------------------------OBJECT INITIALIZATION------------------------------------------------------------------------------------------------------//

// Initializing the esp8266 Object using Software Serial Class
SoftwareSerial esp8266(2, 3); // RX, TX pins on STM32F446RE (you can use any available pins)

// Initializing the AESLib Object using AESLib Class
AESLib aesLib;

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

void ESP_Init(){

  // Initializing the ESP8266
  esp8266.println(ESPReset);                // Resetting...
  delay(3000);
  esp8266.println(ESPAT);                   // Check status by sending AT...
  delay(2000);
  esp8266.println(ESPChangeMode);           // Setting ESP Mode 1...
  delay(3000);
  esp8266.println(ESPGetWifi);              // Connecting to Wifi...
  delay(5000);
 
}

void TransmitJson(String encrypted){

  payload = "{\"encrypted\" : \""+encrypted+"\"}";

  String ESPPost = "POST /check HTTP/1.1\r\nHost: 192.168.0.106\r\nContent-Type: application/json\r\nContent-Length:"+String(payload.length())+"\r\n\r\n"+String(payload)+"\r\n";
  String ESPSendLength = "AT+CIPSEND="+String(ESPPost.length())+"\r\n";

  // TCP Transmission
  esp8266.println(ESPBeginTransmission);    // Begin TCP Transmission...
  delay(2000);
  esp8266.println(ESPSendLength);           // Length of HTTP Request Data...
  delay(1000);
  esp8266.println(ESPPost);                 // Sending HTTP POST Request...
  delay(3000);
  esp8266.println(ESPEndTransmission);      // Ending the TCP Transmission...
  delay(3000);
   
}

//--------------------------------------------FUNCTION DECLARATIONS------------------------------------------------------------------------------------------------------//



//-----------------------------------------------SETUP FUNCTION----------------------------------------------------------------------------------------------------------//

void setup() {
  // Begin Serial Communication
  Serial.begin(115200);

  // Begin esp8266 Communication
  esp8266.begin(115200);

  delay(1000);

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

  ESP_Init();
 
}

//-----------------------------------------------SETUP FUNCTION----------------------------------------------------------------------------------------------------------//



//-----------------------------------------------LOOP FUNCTION-----------------------------------------------------------------------------------------------------------//

void loop() {

  // Sensor Readings Begin

  Data = "{\"Temperature\": \"hi\", \"Humidity\": \"hi\", \"Status\": \"hi\"}";
 
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


 
  // Encrypted Payload Transmission Begin
 
  TransmitJson(encrypted);
 
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

  // Status Printing on Serial terminal End
}

//-----------------------------------------------LOOP FUNCTION-----------------------------------------------------------------------------------------------------------//