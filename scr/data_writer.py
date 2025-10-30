import csv
import json
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

class DataWriter:
    def __init__(self, format="csv"):
        self.format = format.lower()
        self.file = None
        self.writer = None
        self.filename = LOG_DIR / f"vehicle_log.{self.format}"

        if self.format == "csv":
            self.file = open(self.filename, "w", newline="")
            self.writer = csv.DictWriter(self.file, fieldnames=["timestamp", "speed_kph", "rpm", "fuel_level_percent"])
            self.writer.writeheader()
        elif self.format == "json":
            self.file = open(self.filename, "w")
            self.file.write("[\n")
        else:
            raise ValueError("Unsupported format: choose 'csv' or 'json'")

    def write(self, data):
        if self.format == "csv":
            self.writer.writerow(data)
        elif self.format == "json":
            json.dump(data, self.file)
            self.file.write(",\n")

    def close(self):
        if self.format == "json":
            self.file.write("{}]")
        if self.file:
            self.file.close()
