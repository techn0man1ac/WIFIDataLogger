import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tkinter as tk
from tkinter import filedialog
import sqlite3

# Function for selecting the absolute path to the database file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("SQLite files", "*.db")])
    if file_path:
        plot_data(file_path)
        root.destroy()  # Close the program window after processing the file

# Function for plotting data based on the selected database file
def plot_data(file_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(file_path)
    c = conn.cursor()

    # Retrieve data from the database
    c.execute("SELECT * FROM wifi_signal")
    data = c.fetchall()

    # Close the database connection
    conn.close()

    # Create a DataFrame with the data
    df = pd.DataFrame(data, columns=['id', 'ssid', 'rssi', 'timestamp'])
    # Convert the 'timestamp' column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot graphs for each access point
    fig, ax = plt.subplots()
    for ssid, group in df.groupby('ssid'):
        ax.plot(group['timestamp'], group['rssi'], label=ssid)

    # Set date format on x-axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

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