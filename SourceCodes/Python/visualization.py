import json
import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з JSON файлу
with open("C:/Projects/vscode-basics/GoIT-Python-Data-Science/MyProjects/ESP_To_Python/SourceCodes/Python/data1.json", "r") as file:
    data = json.load(file)

# Створення пустого списку для даних про точки доступу
access_points = []

# Розбір кожного запису в JSON та додавання до списку точок доступу
for entry in data:
    timestamp = entry["timestamp"]
    for device in entry["devices"]:
        ssid = device["ssid"]
        rssi = device["rssi"]
        access_points.append({"timestamp": timestamp, "ssid": ssid, "rssi": rssi})

# Створення DataFrame з даними
df = pd.DataFrame(access_points)

# Перетворення стовбця 'timestamp' у формат дати та часу
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Побудова графіків для кожної точки доступу
for ssid, group in df.groupby('ssid'):
    plt.plot(group['timestamp'], group['rssi'], label=ssid)

# Додавання підписів до графіка
plt.title('Wi-Fi Signal Strength Over Time')
plt.xlabel('Time')
plt.ylabel('Signal Strength (RSSI)')
plt.grid(True)
plt.legend()
plt.show()
