#!/usr/bin/env python3
"""
Vehicle Data Logger for EB corbos Linux
---------------------------------------
Reads OBD-II/CAN bus data and logs it to CSV or JSON.
"""

import time
import obd
from data_writer import DataWriter
from config import LOG_INTERVAL, PARAMETERS

def main():
    print("🚗 Starting Vehicle Data Logger...")
    
    # Connect to OBD-II port
    connection = obd.OBD()  # Auto-connect via serial/USB
    if not connection.is_connected():
        print("❌ Could not connect to OBD-II interface.")
        return

    writer = DataWriter(format="csv")

    try:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            data = {"timestamp": timestamp}

            for name, command in PARAMETERS.items():
                response = connection.query(command)
                data[name] = response.value.magnitude if response.value else None

            writer.write(data)
            print(f"✅ Logged: {data}")
            time.sleep(LOG_INTERVAL)

    except KeyboardInterrupt:
        print("\n🛑 Logging stopped by user.")
    finally:
        connection.close()
        writer.close()

if __name__ == "__main__":
    main()
