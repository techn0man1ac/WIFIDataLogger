[![UA_version_README](https://raw.githubusercontent.com/techn0man1ac/WIFIDataLogger/main/imgs/Flags/UA%402x.png)](https://github.com/techn0man1ac/WIFIDataLogger/blob/main/README_UA.md)
[![GB_version_README](https://raw.githubusercontent.com/techn0man1ac/WIFIDataLogger/main/imgs/Flags/GB%402x.png)](https://github.com/techn0man1ac/WIFIDataLogger/)

# ESP8266 WiFi signal logger

![Program datalogger screen](https://raw.githubusercontent.com/techn0man1ac/WIFIDataLogger/main/imgs/image.png)

This project enables logging of WiFi signal strength data from ESP8266 devices. The ESP8266 device scans for nearby WiFi networks and sends the signal strength data to a Python program via HTTP GET requests. The Python program displays the data in real-time using a graphical user interface (GUI) built with Tkinter and saves it to a JSON file for further analysis.

## Data visualizations

This project includes data visualizations to help analyze Wi-Fi signal strength over time. Below are screenshots showcasing the visualizations:

![Data visualization all](https://raw.githubusercontent.com/techn0man1ac/WIFIDataLogger/main/imgs/Figure_1.png)

It displays the signal strength of all detected networks.

![Data visualization one](https://raw.githubusercontent.com/techn0man1ac/WIFIDataLogger/main/imgs/Figure_2.png)

It provides detailed information about the signal strength variations for the selected network.

## Video demonstration

https://www.youtube.com/watch?v=217ZRDhaqyE

## Features

- Logs WiFi signal strength data from ESP8266 devices
- Real-time display of data using a GUI
- Saves data to a JSON file for analysis
- Polls WiFi signal strength data from an ESP8266 device.
- Provides a graphical user interface for starting and stopping data logging.
- Offers data visualization using matplotlib.

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

## JSON Data Format

Please note that the program generates a JSON file with an invalid format due to missing square brackets at the beginning and end of the file. This is because each record in the JSON file represents a single scan of WiFi networks by the ESP8266 device. However, the data visualization program is designed to handle this issue and can still read the JSON file correctly.

## Project Version V0.2

Everything mentioned above applies to version V0.1, but in V0.2, there have been significant conceptual changes, namely:

- A local web server was created (using the Flask framework).
- A database (*.db) was created where the generated signal strength and access point name are recorded in JSON format (on the ESP8266 side).
- The ESP8266 generates a POST request, sending data to the web server in this way.
- The visualization program opens the database in *.db format.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to ChatGPT for assistance with the project.
