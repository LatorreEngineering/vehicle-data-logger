#!/usr/bin/env python3
"""
visualizer.py
-------------
Real-time visualization tool for the Vehicle Data Logger.

It reads from `logs/vehicle_log.csv` and continuously plots
parameters like speed (km/h), RPM, and fuel level using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

LOG_FILE = Path("logs/vehicle_log.csv")

def animate(i):
    """Refresh the plot every interval."""
    try:
        data = pd.read_csv(LOG_FILE)

        if data.empty:
            return

        plt.cla()  # Clear previous frame

        # Plot speed and RPM on primary axis
        plt.plot(data["timestamp"], data["speed_kph"], label="Speed (km/h)", linewidth=2)
        plt.plot(data["timestamp"], data["rpm"], label="RPM", linewidth=2)

        # Optionally plot fuel level if available
        if "fuel_level_percent" in data.columns:
            plt.plot(data["timestamp"], data["fuel_level_percent"], label="Fuel Level (%)", linestyle="--")

        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("🚗 Vehicle Telemetry (Live View)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.legend()
        plt.grid(True)

    except FileNotFoundError:
        plt.cla()
        plt.text(0.5, 0.5, "Waiting for log data...", ha='center', va='center', fontsize=14)
    except Exception as e:
        plt.cla()
        plt.text(0.5, 0.5, f"Error: {e}", ha='center', va='center', fontsize=12, color='red')

def main():
    print("📊 Starting real-time vehicle data visualization...")
    plt.figure(figsize=(10, 6))
    ani = FuncAnimation(plt.gcf(), animate, interval=2000)  # refresh every 2 seconds
    plt.show()

if __name__ == "__main__":
    main()
