/*
  Tech01 simple python WiFi signal logger By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/WIFIDataLogger
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
*/

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ArduinoJson.h> // ArduinoJson-7.0.4

const char* ssid = "YOUSSID";
const char* password = "YOUPASSWORD";

ESP8266WebServer server(80);

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, 1); // LED off
  Serial.begin(115200);

  // Connect to Wi-Fi network
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Start the web server
  server.on("/devices", HTTP_GET, handleDevices);
  server.begin();

  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
  digitalWrite(LED_BUILTIN, 1); // LED off
}

void handleDevices() {

  // Create a dynamic JSON buffer
  DynamicJsonDocument jsonBuffer(1024);

  // Create a JSON array to store Wi-Fi network information
  JsonArray devices = jsonBuffer.createNestedArray("devices");

  // Scan Wi-Fi networks
  int numNetworks = WiFi.scanNetworks();

  // Add information about each device to the JSON array
  for (int i = 0; i < numNetworks; i++) {
    JsonObject device = devices.createNestedObject();
    device["ssid"] = WiFi.SSID(i);
    device["rssi"] = WiFi.RSSI(i);
  }
  digitalWrite(LED_BUILTIN, 0); // LED on
  // Send data in JSON format
  String response;
  serializeJson(jsonBuffer, response);
  server.send(200, "application/json", response);
}
