# ESP8266 WiFi signal logger

![Program screen](https://raw.githubusercontent.com/techn0man1ac/WIFIDataLogger/main/imgs/image.png)

This project enables logging of WiFi signal strength data from ESP8266 devices. The ESP8266 device scans for nearby WiFi networks and sends the signal strength data to a Python program via HTTP GET requests. The Python program displays the data in real-time using a graphical user interface (GUI) built with Tkinter and saves it to a JSON file for further analysis.

## Video demonstration

https://www.youtube.com/shorts/KOSmo48dc8E

## Features

- Logs WiFi signal strength data from ESP8266 devices
- Real-time display of data using a GUI
- Saves data to a JSON file for analysis

## Usage

1. Connect your ESP8266 device to your WiFi network.
2. Run the Python program on your computer.
3. Start logging on the Python program's GUI interface.
4. The ESP8266 device will periodically scan for nearby WiFi networks and send the signal strength data to the Python program.
5. Stop logging when you're done.

## Requirements

- Python 3.x
- Requests library
- Tkinter library
- ESP8266 device(install ArduinoJson 7.0.4 library for Arduino IDE)

## License

This project is licensed under the MIT License.

