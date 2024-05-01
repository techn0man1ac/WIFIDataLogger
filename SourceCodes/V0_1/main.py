'''
  Tech01 simple python WiFi signal logger By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/WIFIDataLogger
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
'''

import requests
import threading
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import json


# Global variables
esp8266_ip = "192.168.0.110"  # Default IP address of ESP8266
url = f"http://{esp8266_ip}/devices"  # Default URL to fetch data
is_polling = False  # Variable to determine whether ESP polling is being executed
cycles = 0  # Counter of cycles

# Function to start polling ESP
def start_polling():
    global is_polling, esp8266_ip, url
    esp8266_ip = ip_entry.get()  # Get the entered IP address
    url = f"http://{esp8266_ip}/devices"  # Update the URL with the entered IP address
    is_polling = True
    threading.Thread(target=poll_esp).start()

# Function to stop polling ESP
def stop_polling():
    global is_polling
    is_polling = False

# Function to perform ESP polling
def poll_esp():
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

# Function to save data to the selected file
def save_data(data):
    file_path = file_entry.get()  # Get the entered file path
    if not file_path:
        file_path = filedialog.asksaveasfilename(defaultextension=".json", initialfile="data.json")
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
    with open(file_path, "a") as file:
        json.dump(data, file)  # Write JSON data to file
        file.write(",\n")  # Add comma and newline

# Function to update GUI with message
def update_gui(message):
    response_label.config(text=message)

# Main function to create GUI
def main():
    global response_label, ip_entry, file_entry

    root = tk.Tk()
    root.title("WiFi Signal Logging")
    root.geometry("400x350")

    ip_label = tk.Label(root, text="Enter ESP8266 IP Address:")
    ip_label.pack(pady=5)
    ip_entry = tk.Entry(root)
    ip_entry.insert(0, esp8266_ip)  # Pre-fill with default IP address
    ip_entry.pack(pady=5)

    file_label = tk.Label(root, text="Enter File Path:")
    file_label.pack(pady=5)
    file_entry = tk.Entry(root)
    file_entry.pack(pady=5)

    browse_button = tk.Button(root, text="Browse", command=browse_file)
    browse_button.pack(pady=5)

    start_button = tk.Button(root, text="Start Logging", command=start_polling)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop Logging", command=stop_polling)
    stop_button.pack(pady=5)

    response_label = tk.Label(root, text="", wraplength=380, justify="center")
    response_label.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()

# Function to browse and select file
def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", initialfile="data.json")
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

if __name__ == "__main__":
    main()