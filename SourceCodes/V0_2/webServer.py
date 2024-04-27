from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Функція для створення таблиці в базі даних SQLite
def create_table():
    conn = sqlite3.connect('MyProjects/ESP_To_Python/SourceCodes/Python/V0_2/wifi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS wifi_signal
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  ssid TEXT NOT NULL,
                  signal_strength INTEGER NOT NULL,
                  timestamp TEXT NOT NULL)''')  # Змінено тип поля timestamp на TEXT
    conn.commit()
    conn.close()

# Маршрут для додавання даних про рівень сигналу Wi-Fi до бази даних
@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json()  # Отримання JSON даних з POST запиту
    conn = sqlite3.connect('MyProjects/ESP_To_Python/SourceCodes/Python/V0_2/wifi_data.db')
    c = conn.cursor()
    for network in data['networks']:
        ssid = network['ssid']
        signal_strength = network['signal_strength']
        # Отримання поточного місцевого часу
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute('''INSERT INTO wifi_signal (ssid, signal_strength, timestamp) 
                     VALUES (?, ?, ?)''', (ssid, signal_strength, current_time))
    conn.commit()
    conn.close()
    return 'Data added successfully!'

# Маршрут для відображення даних з бази даних
@app.route('/view_data')
def view_data():
    conn = sqlite3.connect('MyProjects/ESP_To_Python/SourceCodes/Python/V0_2/wifi_data.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM wifi_signal''')
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    create_table()  # Створення таблиці при запуску програми
    app.run(debug=True, host="192.168.0.101") # Параметр host вказує на адресу сервера