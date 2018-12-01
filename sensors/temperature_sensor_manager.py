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
        super().__init__()
        self._sensor_readings = self.session.query(TemperatureReading).all()
        self._last_sequence_num = len(self._sensor_readings)

    def _load_reading_row(self, row):
        """ Loads list into a TemperatureReading object """

        reading_datetime = datetime.datetime.strptime(row[TemperatureSensorManager.DATETIME_INDEX], "%Y-%m-%d %H:%M:%S.%f")

        temp_reading = TemperatureReading(reading_datetime,
                               int(row[TemperatureSensorManager.SEQ_NUM_INDEX]),
                               row[TemperatureSensorManager.SENSOR_NAME_INDEX],
                               float(row[TemperatureSensorManager.LOW_INDEX]),
                               float(row[TemperatureSensorManager.AVG_INDEX]),
                               float(row[TemperatureSensorManager.HIGH_INDEX]),
                               row[TemperatureSensorManager.STATUS_INDEX])
        return temp_reading
    
   