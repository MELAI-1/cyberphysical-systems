"""
Temperature Data Visualizer
Create charts and graphs from sensor data

Dependencies: pip install matplotlib pandas
"""

import csv
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import sys


class SensorDataVisualizer:
    """Visualize sensor data from CSV or JSON files"""
    
    def __init__(self, data_file):
        """
        Initialize visualizer with data file
        
        Args:
            data_file: Path to CSV or JSON file
        """
        self.data_file = data_file
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load data from file"""
        if self.data_file.endswith('.csv'):
            self.df = pd.read_csv(self.data_file)
            self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        elif self.data_file.endswith('.json'):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            self.df = pd.DataFrame(data)
            self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        else:
            raise ValueError("Unsupported file format")
    
    def plot_temperature(self, title="Temperature Over Time"):
        """Plot temperature readings over time"""
        plt.figure(figsize=(12, 6))
        
        if 'Timestamp' in self.df.columns:
            x = self.df['Timestamp']
            y = self.df['Temperature_C']
        else:
            x = self.df['timestamp']
            y = self.df['temperature']
        
        plt.plot(x, y, marker='o', linestyle='-', linewidth=2, markersize=6)
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xlabel('Time', fontsize=12)
        plt.ylabel('Temperature (°C)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return plt
    
    def plot_statistics(self):
        """Plot temperature statistics"""
        if 'Temperature_C' in self.df.columns:
            temps = self.df['Temperature_C']
        else:
            temps = self.df['temperature']
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Histogram
        axes[0, 0].hist(temps, bins=10, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Temperature Distribution', fontweight='bold')
        axes[0, 0].set_xlabel('Temperature (°C)')
        axes[0, 0].set_ylabel('Frequency')
        
        # Box plot
        axes[0, 1].boxplot(temps)
        axes[0, 1].set_title('Temperature Box Plot', fontweight='bold')
        axes[0, 1].set_ylabel('Temperature (°C)')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Statistics text
        stats_text = f"""
        Statistics Summary:
        ━━━━━━━━━━━━━━━━━━
        Count: {len(temps)}
        Min: {temps.min():.2f}°C
        Max: {temps.max():.2f}°C
        Mean: {temps.mean():.2f}°C
        Median: {temps.median():.2f}°C
        Std Dev: {temps.std():.2f}°C
        """
        
        axes[1, 0].text(0.1, 0.5, stats_text, fontsize=11, 
                        verticalalignment='center', family='monospace',
                        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        axes[1, 0].axis('off')
        
        # Moving average
        if 'Timestamp' in self.df.columns:
            x = self.df['Timestamp']
        else:
            x = range(len(temps))
        
        moving_avg = temps.rolling(window=3, min_periods=1).mean()
        axes[1, 1].plot(x, temps, marker='o', label='Actual', alpha=0.6)
        axes[1, 1].plot(x, moving_avg, color='red', label='3-point Moving Avg', linewidth=2)
        axes[1, 1].set_title('Temperature with Moving Average', fontweight='bold')
        axes[1, 1].set_xlabel('Time')
        axes[1, 1].set_ylabel('Temperature (°C)')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return plt
    
    def print_summary(self):
        """Print data summary"""
        if 'Temperature_C' in self.df.columns:
            temps = self.df['Temperature_C']
        else:
            temps = self.df['temperature']
        
        print("\n" + "=" * 50)
        print("📊 DATA SUMMARY")
        print("=" * 50)
        print(f"Total Readings: {len(temps)}")
        print(f"Temperature Range: {temps.min():.2f}°C - {temps.max():.2f}°C")
        print(f"Average Temperature: {temps.mean():.2f}°C")
        print(f"Median Temperature: {temps.median():.2f}°C")
        print(f"Std Deviation: {temps.std():.2f}°C")
        print("=" * 50 + "\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python visualize_sensor_data.py <data_file> [--stats]")
        print("Example: python visualize_sensor_data.py sensor_data_20240630_120000.csv")
        return
    
    data_file = sys.argv[1]
    show_stats = '--stats' in sys.argv or '-s' in sys.argv
    
    try:
        viz = SensorDataVisualizer(data_file)
        viz.print_summary()
        
        # Plot temperature
        print("Generating temperature plot...")
        plt = viz.plot_temperature()
        plt.show()
        
        # Plot statistics if requested
        if show_stats:
            print("Generating statistics plots...")
            plt = viz.plot_statistics()
            plt.show()
        
        print("✅ Visualization complete!")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{data_file}' not found")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
