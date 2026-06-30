# 🌡️ Temperature Sensor Reader - Beginner Project

## 📖 Overview

This is your **first practical CPS project**: a complete temperature sensor data acquisition, logging, and visualization system.

**What You'll Learn:**
- Reading sensor data
- Data storage (CSV, JSON)
- Basic statistics calculation
- Data visualization
- Python OOP principles

**Difficulty:** ⭐ Beginner  
**Time to Complete:** 30-60 minutes  
**Language:** Python

---

## 🎯 Project Objectives

1. ✅ Simulate temperature sensor readings
2. ✅ Log sensor data with timestamps
3. ✅ Calculate statistics (min, max, average, etc.)
4. ✅ Export data to CSV and JSON
5. ✅ Visualize data with charts

---

## 📁 Files

- **`temperature_sensor_reader.py`** - Main data acquisition and logging
- **`visualize_sensor_data.py`** - Data visualization tool
- **`requirements.txt`** - Python dependencies

---

## 🚀 Quick Start

### **Step 1: Install Dependencies**
```bash
cd sensors
pip install -r requirements.txt
```

### **Step 2: Run Temperature Monitor**
```bash
python temperature_sensor_reader.py
```

**Expected Output:**
```
==================================================
Temperature Sensor Monitoring System
==================================================
Sensor Type: DHT22
Reading Interval: 2s
Total Readings: 20
==================================================
[14:23:45] Temp: 22.15°C | Humidity: 52.30%
[14:23:47] Temp: 22.45°C | Humidity: 51.80%
[14:23:49] Temp: 22.35°C | Humidity: 52.10%
...
==================================================
📊 STATISTICS:
  Total Readings: 20
  Min Temperature: 21.98°C
  Max Temperature: 22.87°C
  Average Temperature: 22.45°C
  Median Temperature: 22.42°C
  Std Deviation: 0.25°C

💾 Data Files:
  CSV: sensor_data_20240630_123456.csv
  JSON: sensor_data_20240630_123456.json
==================================================
```

### **Step 3: Visualize Data**
```bash
# Generate temperature plot
python visualize_sensor_data.py sensor_data_*.csv

# Include statistics plots
python visualize_sensor_data.py sensor_data_*.csv --stats
```

---

## 📊 What the Data Looks Like

### **CSV Format**
```csv
Timestamp,Temperature_C,Humidity_%,Reading_Number
2024-06-30T14:23:45.123456,22.15,52.30,1
2024-06-30T14:23:47.234567,22.45,51.80,2
2024-06-30T14:23:49.345678,22.35,52.10,3
...
```

### **JSON Format**
```json
[
  {
    "timestamp": "2024-06-30T14:23:45.123456",
    "temperature": 22.15,
    "humidity": 52.30,
    "reading_num": 1
  },
  ...
]
```

---

## 🔧 How the Code Works

### **TemperatureSensor Class**
- Represents the physical sensor
- `read_temperature()` - Gets current temperature
- Supports simulated and real readings

```python
sensor = TemperatureSensor(sensor_type="DHT22")
temp = sensor.read_temperature(use_simulation=True)
```

### **SensorDataLogger Class**
- Logs readings with timestamps
- Stores data in memory (deque)
- Exports to CSV and JSON
- Calculates statistics

```python
logger = SensorDataLogger(max_readings=100)
logger.log_reading(temperature=22.5, humidity=52.0, reading_num=1)
stats = logger.get_statistics()
```

### **TemperatureMonitor Class**
- Main orchestration class
- Coordinates sensor and logger
- Handles timing and display

```python
monitor = TemperatureMonitor()
monitor.run(num_readings=20, interval=2)
```

---

## 🎓 Learning Points

### **1. Sensor Simulation**
The current code simulates sensor readings. In real applications, you'd replace this with actual hardware communication.

### **2. Data Logging**
Professional systems log data with:
- Timestamps
- Reading numbers
- Multiple formats (CSV for spreadsheets, JSON for APIs)

### **3. Statistics**
Understanding basic statistics is crucial for sensor data:
- **Mean** - Average value
- **Median** - Middle value
- **Std Dev** - Variability
- **Min/Max** - Range

### **4. Data Visualization**
Visual representation reveals patterns:
- Temperature trends
- Anomalies
- Distribution

---

## 📈 Visualization Examples

The visualizer generates:

1. **Temperature Over Time** - Line plot showing temperature changes
2. **Distribution** - Histogram of temperature values
3. **Box Plot** - Statistical summary visualization
4. **Moving Average** - Smoothed trend line
5. **Statistics Summary** - Numerical summary

---

## 🔌 Next Steps: Real Hardware

To use with actual sensors:

### **DHT22 Sensor**
```python
import Adafruit_DHT

def read_temperature(self, use_simulation=False):
    if not use_simulation:
        humidity, temperature = Adafruit_DHT.read_retry(
            Adafruit_DHT.DHT22, 
            self.pin
        )
        return temperature
```

### **LM35 Temperature Sensor**
```python
import board
import adafruit_ads1x15.analog_in as AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS

# Read via ADC converter
channel = AnalogIn(ads, ADS.P0)
voltage = channel.voltage
temperature = voltage / 0.01  # LM35: 10mV per °C
```

---

## 🧪 Exercises to Extend This Project

### **Easy:**
1. Add humidity threshold alerts
2. Change sampling interval
3. Export to different formats
4. Add multiple sensors

### **Medium:**
1. Store data in SQLite database
2. Create web dashboard with Flask
3. Add email alerts for anomalies
4. Implement data averaging

### **Advanced:**
1. Machine learning anomaly detection
2. Cloud data sync (AWS/Azure)
3. Real-time streaming dashboard
4. Multi-sensor fusion

---

## 📚 Resources

- **Python CSV Module** - https://docs.python.org/3/library/csv.html
- **Pandas Documentation** - https://pandas.pydata.org/
- **Matplotlib Plotting** - https://matplotlib.org/
- **DHT22 Adafruit Library** - https://github.com/adafruit/Adafruit_Python_DHT

---

## 🐛 Troubleshooting

### **"No module named 'matplotlib'"**
```bash
pip install matplotlib pandas
```

### **CSV file not found**
Make sure you've run the temperature reader first to generate data files.

### **Charts not displaying**
You might need to install a backend. Try:
```bash
pip install PyQt5
```

---

## ✅ Success Criteria

You've completed this project when:
- ✅ Temperature monitor runs without errors
- ✅ CSV file is generated with sensor data
- ✅ JSON file export works
- ✅ Statistics are calculated correctly
- ✅ Charts display temperature trends
- ✅ You understand each class and function

---

## 🎉 Congratulations!

You've built your first CPS project! This foundation will help you:
- Understand sensor interfaces
- Handle time-series data
- Visualize real-world measurements
- Progress to more complex systems

---

**Next Challenge:** Modify the code to support multiple sensors simultaneously! 🚀
