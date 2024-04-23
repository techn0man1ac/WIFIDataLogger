'''
Thank's ChatGPT for help, by Serhii Trush with MIT Licence
'''

import requests
import threading
import tkinter as tk

esp8266_ip = "192.168.0.110"  # IP-addres ESP8266
url = f"http://{esp8266_ip}/inline"  # URL to retrieve data
is_polling = False  # A variable to determine whether ESP polling is performed
cycles = 0  # Counter of  cycles

def start_polling():
    global is_polling, cycles
    is_polling = True
    threading.Thread(target=poll_esp).start()

def stop_polling():
    global is_polling
    is_polling = False

def poll_esp():
    global cycles
    while is_polling:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.text
                with open("MyProjects/ESP_To_Python/SourceCodes/Python/data.txt", "a") as file:  # Opening a file and add the data
                    file.write(data + "\n")  # Write data on a new line
                    print(f"Datas {data} successfully added to the file data.txt {cycles} cycles")
                response_label.config(text=data)
                cycles += 1
                cycle_label.config(text=f"Cycles: {cycles}")
            else:
                response_label.config(text=f"Error: {response.status_code}")
        except Exception as e:
            response_label.config(text=f"An error occurred while executing the request: {e}")

def main():
    global response_label, cycle_label

    root = tk.Tk()
    root.title("WiFi Signal logging")
    root.geometry("400x200")

    start_button = tk.Button(root, text="Start logging", command=start_polling)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop logging", command=stop_polling)
    stop_button.pack(pady=10)

    response_label = tk.Label(root, text="", wraplength=380, justify="center")
    response_label.pack(fill="both", expand=True, padx=10, pady=10)

    cycle_label = tk.Label(root, text="Cycles: 0")
    cycle_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
