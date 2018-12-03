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
        self._last_sequence_num = 0
        for reading in self._sensor_readings:
                        
            if reading.get_sequence_num() > self._last_sequence_num:
                self._last_sequence_num = reading.get_sequence_num()


    

    