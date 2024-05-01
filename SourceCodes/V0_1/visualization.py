'''
  Tech01 simple python WiFi signal logger By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/WIFIDataLogger
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
'''

import json
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Function for selecting the absolute path to the JSON file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        plot_data(file_path)
        root.destroy()  # Close the program window after processing the file

# Function for plotting data based on the selected file
def plot_data(file_path):
    # Load data from the JSON file
    with open(file_path, "r") as file:
        # Read the entire file content
        content = file.read()
        # Replace the last comma with a closing square bracket
        content = content.rsplit(',', 1)[0] + ']'
        # Add an opening square bracket at the beginning
        content = '[' + content
        # Parse JSON data
        data = json.loads(content)

    # Create an empty list for access point data
    access_points = []

    # Parse each entry in JSON and add to the list of access points
    for entry in data:
        timestamp = entry["timestamp"]
        for device in entry["devices"]:
            ssid = device["ssid"]
            rssi = device["rssi"]
            access_points.append({"timestamp": timestamp, "ssid": ssid, "rssi": rssi})

    # Create a DataFrame with the data
    df = pd.DataFrame(access_points)

    # Convert the 'timestamp' column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot graphs for each access point
    for ssid, group in df.groupby('ssid'):
        plt.plot(group['timestamp'], group['rssi'], label=ssid)

    # Add labels to the plot
    plt.title('Wi-Fi Signal Strength Over Time')
    plt.xlabel('Time')
    plt.ylabel('Signal Strength (RSSI)')
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.close()  # Close the plot after displaying it

# Function to create and run the GUI
def main():
    global root
    root = tk.Tk()
    root.title("Select File")
    root.geometry("300x100")

    select_button = tk.Button(root, text="Select File", command=select_file)
    select_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
