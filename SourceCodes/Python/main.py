'''
  Tech01 simple python WiFi signal logger By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/WIFIDataLogger
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
'''

import requests
import threading
import tkinter as tk
from datetime import datetime

# Global variables
esp8266_ip = "192.168.0.110"  # IP address of ESP8266
url = f"http://{esp8266_ip}/devices"  # URL to fetch data
is_polling = False  # Variable to determine whether ESP polling is being executed
cycles = 0  # Counter of cycles


def start_polling():
    """Start polling ESP."""
    global is_polling
    is_polling = True
    threading.Thread(target=poll_esp).start()


def stop_polling():
    """Stop polling ESP."""
    global is_polling
    is_polling = False


def poll_esp():
    """Perform ESP polling."""
    global cycles
    while is_polling:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()  # Get JSON data
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time in string format
                data_with_timestamp = {"timestamp": timestamp, **data}  # Add timestamp to JSON data
                save_data(data_with_timestamp)  # Save data
                cycles += 1
                update_gui(f"Data write {cycles} cycles {data_with_timestamp}")
            else:
                update_gui(f"Error: {response.status_code}")
        except Exception as e:
            update_gui(f"An error occurred while executing the request: {e}")


def save_data(data):
    """Save data to the data.json file."""
    with open("MyProjects/ESP_To_Python/SourceCodes/Python/data.json", "a") as file:
        file.write(str(data) + ", " + '\n')


def update_gui(message):
    """Update GUI with message."""
    response_label.config(text=message)


def main():
    """Main function to create GUI."""
    global response_label

    root = tk.Tk()
    root.title("WiFi Signal Logging")
    root.geometry("400x220")

    start_button = tk.Button(root, text="Start Logging", command=start_polling)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop Logging", command=stop_polling)
    stop_button.pack(pady=10)

    response_label = tk.Label(root, text="", wraplength=380, justify="center")
    response_label.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
