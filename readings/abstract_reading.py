from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from base import Base

class AbstractReading(Base):
    """Mapping for both reading table"""

    __abstract__ = True

    id = Column(Integer,primary_key = True)
    timestamp = Column(DateTime, nullable=False)
    model = Column(String(250),nullable=False)
    min_reading = Column(Integer,nullable=False)
    avg_reading = Column(Integer,nullable=False)
    max_reading = Column(Integer,nullable=False)
    status = Column(String(250),nullable=False)

    def __init__(self, date, seq_num, sensor_name,
                lowest_temp, avg_temp, highest_temp, status):
        """ Initializes the sensor reading """
        self.id = seq_num
        self.timestamp = date
        self.model = sensor_name
        self.min_reading = lowest_temp
        self.avg_reading = avg_temp
        self.max_reading = highest_temp
        self.status = status

    def get_timestamp(self):
        """ Getter for timestamp """
        return self.timestamp

    def get_sensor_model(self):
        """ Getter for sensor model """
        return self.model

    def get_sequence_num(self):
        """ Getter for sequence number """
        return self.id

    def set_sequence_num(self, value):
        """ Getter for sequence number """
        self.sequence_num = value

    def get_min_value(self):
        """ Getter for the minimum temperature """
        return self.min_reading

    def get_avg_value(self):
        """ Getter for the average temperature """
        return self.avg_reading

    def get_max_value(self):
        """ Getter for the maximum temperature """
        return self.max_reading

    def get_status(self):
        return self.status

    def get_range(self):
        """ Getter for the temperature range """
        return self._max - self._min

    def is_error(self):
        """ Abstract Method - Is Reading and Error """
        raise NotImplementedError("Must be implemented")

    def get_error_msg(self):
        """ Abstract Method - Get Error Readings """
        raise NotImplementedError("Must be implemented")

    def to_json(self):
        """ TODO """
        return json.dumps({"id":self.id,"timestamp":str(self._timestamp),"sensor_model":self._sensor_model,"sequence_num":self._sequence_num,
                           "min_reading":self._min,"avg_reading":self._avg, "max_reading":self._max, "status":self._status})

    def to_dict(self):
        """ TODO """
        return {"id":self.id,"timestamp":str(self._timestamp),"sensor_model":self._sensor_model,"sequence_num":self._sequence_num,
                           "min_reading":self._min,"avg_reading":self._avg, "max_reading":self._max, "status":self._status}


