#
# This is a script to read in and process temperature sensor readings
#
# Author: Joe Developer
# Version: 1.0
#
from sensors.temperature_sensor import TemperatureSensorManager
from sensors.pressure_sensor import PressureSensorManager
from observers.temp_observer import TempObserver
from observers.pressure_observer import PressureObserver
from observers.audit_observer import AuditObserver

temp_results_file1 = "data/temperature_results.csv"
temp_results_file2 = "data/temperature_results2.csv"
press_results_file1 = "data/pressure_results.csv"
press_results_file2 = "data/pressure_results2.csv"


def main():
    temp_sensor = TemperatureSensorManager()
    temp_observer = TempObserver(temp_sensor)
    temp_audit_observer = AuditObserver(temp_sensor)
    temp_sensor.attach(temp_observer)
    temp_sensor.attach(temp_audit_observer)

    pressure_sensor = PressureSensorManager()
    pressure_observer = PressureObserver(pressure_sensor)
    pressure_audit_observer = AuditObserver(pressure_sensor)
    pressure_sensor.attach(pressure_observer)
    pressure_sensor.attach(pressure_audit_observer)

    temp_sensor.load_readings(temp_results_file1)
    pressure_sensor.load_readings(press_results_file1)

    temp_sensor.load_readings(temp_results_file2)
    pressure_sensor.load_readings(press_results_file2)


if __name__ == "__main__":
    main()
