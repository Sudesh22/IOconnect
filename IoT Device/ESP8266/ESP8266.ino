#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <LiquidCrystal_I2C.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

#define SERVER_IP "physically-secure-condor.ngrok-free.app"

#ifndef STASSID
#define STASSID "SUDESH"
#define STAPSK "sud1ath7"
#endif

LiquidCrystal_I2C lcd(0x27, 16, 2);
WiFiClient client;

// Define NTP Client to get time
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

void setup() {

  Serial.begin(115200);
  
  lcd.init();
  lcd.backlight();
  timeClient.begin();
  timeClient.setTimeOffset(19800);
  
  WiFi.begin(STASSID, STAPSK);

  lcd.clear();
  lcd.setCursor(3, 0);
  lcd.print("Welcome To");
  lcd.setCursor(3, 1);
  lcd.print("IOconnect");

  delay(5000);

  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Connecting to");
  lcd.setCursor(4, 1);
  lcd.print("Network");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  delay(1000);
}

String getTime_(){
  timeClient.update();

  time_t epochTime = timeClient.getEpochTime();  
  String formattedTime = timeClient.getFormattedTime();
  Serial.print("Formatted Time: ");
  Serial.println(formattedTime);  
  
  //Get a time structure
  struct tm *ptm = gmtime ((time_t *)&epochTime); 
  int monthDay = ptm->tm_mday;
  String monthD;
  if (monthDay<10){
    monthD = "0" + String(monthDay);
  }
  else{
    monthD = String(monthDay);
  }
  int currentMonth = ptm->tm_mon+1;
  String currentM;
  if (currentMonth<10){
    currentM = "0" + String(currentMonth);
  }
  else{
    currentM = String(currentMonth);
  }
  int currentYear = ptm->tm_year+1900;
  
  //Print complete date:
  String currentDate = String(currentYear) + "-" + String(currentM) + "-" + String(monthD);
  Serial.print("Current date: ");
  Serial.println(currentDate.substring(2,-1));

  return currentDate.substring(2,-1) + " " + formattedTime;
}

void loop() {
  // wait for WiFi connection
  if ((WiFi.status() == WL_CONNECTED)) {

    HTTPClient http;

          lcd.clear();
          lcd.setCursor(1, 0);
          lcd.print("System Online!");

          String receivedData = Serial.readString();

          if (receivedData == "Date")
          {
          Serial.print(getTime_());
          }
          else{
          
          Serial.print("Received data from Arduino: ");
          Serial.println(receivedData);

          String encrypted, Method, route, hashh = "";
      
          for (int i = 0; i < 4; i++) {
              int commaIndex = receivedData.indexOf(',');
          
              if (commaIndex != -1) {
                  String Substring = receivedData.substring(0, commaIndex);
                  receivedData.remove(0, commaIndex + 1);
                  switch (i){
                    case 0:
                      encrypted = Substring;
                      Serial.println("Encrypted: " + encrypted);
                      break;
                    case 1:
                      hashh = Substring;
                      Serial.println("Hash: " + hashh);
                      break;
                    case 2:
                      Method = Substring;
                      Serial.println("Method: " + Method);
                      break;
                    case 3:
                      route = Substring;
                      Serial.println("Route: " + route);
                      break;
                    default:
                      break;
                  
                  }
              }
          }
      

      Serial.print("[HTTP] begin...\n");
      // configure traged server and url
      http.begin(client, "http://" SERVER_IP "/decode");  // HTTP
      http.addHeader("Content-Type", "application/json");
  
      Serial.print("[HTTP] POST...\n");
      // start connection and send HTTP header and body
      int httpCode = http.POST("{\"encrypted\":\""+encrypted+"\", \"hash\": \""+hashh+"\"}");
  
      // httpCode will be negative on error
      if (httpCode > 0) {
        // HTTP header has been send and Server response header has been handled
        Serial.printf("[HTTP] POST... code: %d\n", httpCode);
  
        // file found at server
        if (httpCode == HTTP_CODE_OK) {
          const String& payload = http.getString();
          Serial.println("received payload:\n<<");
          Serial.println(payload);
          Serial.println(">>");
        }
    }
    else{
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  }
  }
  else{
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("System Offline!");

  }
  delay(5000);
}
