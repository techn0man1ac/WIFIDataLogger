/*
  Tech01 simple python WiFi signal logger V0.2 By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/WIFIDataLogger
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h> // ArduinoJson 7.0.4 https://github.com/bblanchon/ArduinoJson

const char* ssid = "YOUSSID";
const char* password = "YOUPASSWORD";
const char* serverAddress = "192.168.0.101";
const int serverPort = 5000; // Порт вашого сервера

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, 1); // LED off
  Serial.begin(115200);
  delay(10);

  // Connect to Wi-Fi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  digitalWrite(LED_BUILTIN, 1); // LED off
  sendDataToServer();
}

void sendDataToServer() {
  // Sending data to the server
  if (WiFi.status() == WL_CONNECTED) {
    DynamicJsonDocument jsonBuffer(1024);
    JsonArray networks = jsonBuffer.createNestedArray("networks");

    int numNetworks = WiFi.scanNetworks();
    for (int i = 0; i < numNetworks; i++) {
      JsonObject network = networks.createNestedObject();
      network["ssid"] = WiFi.SSID(i);
      network["signal_strength"] = WiFi.RSSI(i);
    }

    WiFiClient client;
    HTTPClient http;
    if (http.begin(client, "http://" + String(serverAddress) + ":" + String(serverPort) + "/add_data")) {
      http.addHeader("Content-Type", "application/json");
      int httpResponseCode = http.POST(jsonBuffer.as<String>());
      if (httpResponseCode > 0) {  
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        String response = http.getString();
        Serial.println(response);
      } else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      digitalWrite(LED_BUILTIN, 0); // LED on
      http.end();
    } else {
      Serial.println("Failed to connect to server");
    }
  }
}
