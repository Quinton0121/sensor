import datetime
from sensors.abstract_sensor_manager import AbstractSensorManager
from readings.pressure_reading import PressureReading


class PressureSensorManager(AbstractSensorManager):
    """ Pressure Sensor Concrete Implementation """

    # CONSTANTS
    DATETIME_INDEX = 0
    SENSOR_NAME_INDEX = 1
    SEQ_NUM_INDEX = 2
    LOW_INDEX = 3
    AVG_INDEX = 4
    HIGH_INDEX = 5
    STATUS_INDEX = 6

    def __init__(self):
        """ Constructor for PressureSensorManager Class """
        super().__init__()
        self._sensor_readings = self.session.query(PressureReading).all()
        self._last_sequence_num = len(self._sensor_readings)

    def _load_reading_row(self, row):
        """ Loads list into a PressureReading object """

        reading_datetime = datetime.datetime.strptime(row[PressureSensorManager.DATETIME_INDEX], "%Y-%m-%d %H:%M")

        pressure_reading = PressureReading(reading_datetime,
                               row[PressureSensorManager.SENSOR_NAME_INDEX],
                               int(row[PressureSensorManager.SEQ_NUM_INDEX]),
                               float(row[PressureSensorManager.LOW_INDEX]),
                               float(row[PressureSensorManager.AVG_INDEX]),
                               float(row[PressureSensorManager.HIGH_INDEX]),
                               row[PressureSensorManager.STATUS_INDEX])

        return pressure_reading

    