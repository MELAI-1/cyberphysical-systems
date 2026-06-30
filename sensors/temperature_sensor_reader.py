"""
Simple Temperature Sensor Reader
Beginner Project - Reading sensor data and storing it

This project demonstrates:
- Reading sensor data from DHT22/LM35
- Storing data with timestamps
- Basic CSV export
- Simple visualization
"""

import time
import csv
import json
from datetime import datetime
from collections import deque
import statistics


class TemperatureSensor:
    """Simulates or interfaces with real temperature sensor"""
    
    def __init__(self, sensor_type="DHT22", pin=17):
        """
        Initialize sensor
        
        Args:
            sensor_type: "DHT22", "LM35", "SIM" (simulated)
            pin: GPIO pin number
        """
        self.sensor_type = sensor_type
        self.pin = pin
        self.last_reading = None
        self.read_count = 0
        
    def read_temperature(self, use_simulation=True):
        """
        Read temperature from sensor
        
        Args:
            use_simulation: Use simulated data if True
            
        Returns:
            float: Temperature in Celsius
        """
        if use_simulation:
            # Simulate sensor reading with slight variation
            import random
            base_temp = 22.5
            noise = random.uniform(-0.5, 0.5)
            return base_temp + noise
        else:
            # Real sensor reading would go here
            # For DHT22:
            # import Adafruit_DHT
            # humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin)
            # return temperature
            pass
    
    def read_humidity(self, use_simulation=True):
        """
        Read humidity from sensor (if available)
        
        Returns:
            float: Humidity percentage
        """
        if use_simulation:
            import random
            return random.uniform(40, 60)
        return None


class SensorDataLogger:
    """Logs sensor data with timestamps"""
    
    def __init__(self, max_readings=100):
        """
        Initialize data logger
        
        Args:
            max_readings: Maximum readings to keep in memory
        """
        self.data = deque(maxlen=max_readings)
        self.filename = f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.initialize_csv()
    
    def initialize_csv(self):
        """Create CSV file with headers"""
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Temperature_C', 'Humidity_%', 'Reading_Number'])
    
    def log_reading(self, temperature, humidity=None, reading_num=None):
        """
        Log a sensor reading
        
        Args:
            temperature: Temperature value
            humidity: Humidity value (optional)
            reading_num: Reading number
        """
        timestamp = datetime.now().isoformat()
        
        # Store in memory
        reading = {
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity,
            'reading_num': reading_num
        }
        self.data.append(reading)
        
        # Write to CSV
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                timestamp,
                f"{temperature:.2f}",
                f"{humidity:.2f}" if humidity else "N/A",
                reading_num if reading_num else "0"
            ])
    
    def get_statistics(self):
        """Calculate statistics from stored readings"""
        if not self.data:
            return None
        
        temps = [reading['temperature'] for reading in self.data]
        
        stats = {
            'count': len(temps),
            'min': min(temps),
            'max': max(temps),
            'avg': statistics.mean(temps),
            'median': statistics.median(temps),
            'stdev': statistics.stdev(temps) if len(temps) > 1 else 0
        }
        return stats
    
    def export_json(self):
        """Export all data as JSON"""
        json_filename = self.filename.replace('.csv', '.json')
        with open(json_filename, 'w') as f:
            json.dump(list(self.data), f, indent=2)
        return json_filename


class TemperatureMonitor:
    """Main monitoring application"""
    
    def __init__(self):
        """Initialize monitoring system"""
        self.sensor = TemperatureSensor()
        self.logger = SensorDataLogger(max_readings=50)
        self.reading_count = 0
    
    def run(self, num_readings=10, interval=1):
        """
        Run monitoring for specified number of readings
        
        Args:
            num_readings: Number of readings to take
            interval: Time between readings in seconds
        """
        print("=" * 50)
        print("Temperature Sensor Monitoring System")
        print("=" * 50)
        print(f"Sensor Type: {self.sensor.sensor_type}")
        print(f"Reading Interval: {interval}s")
        print(f"Total Readings: {num_readings}")
        print("=" * 50)
        
        try:
            for i in range(num_readings):
                self.reading_count += 1
                
                # Read sensor
                temperature = self.sensor.read_temperature(use_simulation=True)
                humidity = self.sensor.read_humidity(use_simulation=True)
                
                # Log data
                self.logger.log_reading(
                    temperature=temperature,
                    humidity=humidity,
                    reading_num=self.reading_count
                )
                
                # Display
                timestamp = datetime.now().strftime('%H:%M:%S')
                print(f"[{timestamp}] Temp: {temperature:.2f}°C | Humidity: {humidity:.2f}%")
                
                # Wait for next reading
                if i < num_readings - 1:
                    time.sleep(interval)
            
            print("\n" + "=" * 50)
            self.print_statistics()
            print("=" * 50)
            
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")
            self.print_statistics()
    
    def print_statistics(self):
        """Print statistics from collected data"""
        stats = self.logger.get_statistics()
        
        if stats:
            print("📊 STATISTICS:")
            print(f"  Total Readings: {stats['count']}")
            print(f"  Min Temperature: {stats['min']:.2f}°C")
            print(f"  Max Temperature: {stats['max']:.2f}°C")
            print(f"  Average Temperature: {stats['avg']:.2f}°C")
            print(f"  Median Temperature: {stats['median']:.2f}°C")
            print(f"  Std Deviation: {stats['stdev']:.2f}°C")
            
            print(f"\n💾 Data Files:")
            print(f"  CSV: {self.logger.filename}")
            json_file = self.logger.export_json()
            print(f"  JSON: {json_file}")


# ============================================================
# QUICK START USAGE
# ============================================================

if __name__ == "__main__":
    # Create and run temperature monitor
    monitor = TemperatureMonitor()
    
    # Collect 20 readings with 2 second intervals
    monitor.run(num_readings=20, interval=2)
    
    print("\n✅ Temperature monitoring complete!")
    print("Check the generated CSV and JSON files for data analysis.")
