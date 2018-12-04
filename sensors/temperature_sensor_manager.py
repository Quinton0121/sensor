import datetime
from sensors.abstract_sensor_manager import AbstractSensorManager
from readings.temperature_reading import TemperatureReading


class TemperatureSensorManager(AbstractSensorManager):
    """ Temperature Sensor concrete implementation """

    # CONSTANTS
    DATETIME_INDEX = 0
    SEQ_NUM_INDEX = 1
    SENSOR_NAME_INDEX = 2
    LOW_INDEX = 3
    AVG_INDEX = 4
    HIGH_INDEX = 5
    STATUS_INDEX = 6

    """ Constructor for TemperatureSensorManager class """
    def __init__(self):
        """ Constructor for PressureSensorManager Class """
        super().__init__(TemperatureReading)

    

    
   