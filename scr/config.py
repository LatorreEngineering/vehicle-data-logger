import obd

# Log every 1 second
LOG_INTERVAL = 1  

# Define which parameters to collect
PARAMETERS = {
    "speed_kph": obd.commands.SPEED,
    "rpm": obd.commands.RPM,
    "fuel_level_percent": obd.commands.FUEL_LEVEL,
}
