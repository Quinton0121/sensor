from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sensors.time_range import TimeRange
from sensors.reading_stats import ReadingStats
from readings.abstract_reading import AbstractReading
from sqlalchemy.pool import SingletonThreadPool


class AbstractSensorManager:
    """ Abstract Implementation of a Sensor """

    def __init__(self):
        """ Initializes the list of sensor readings for the sensor """

        #Engine - allows the session to etablishes the connection to the DB
        self.engine = create_engine("sqlite:///readings.sqlite",poolclass=SingletonThreadPool) 

        #DB Session Maker given a SQLite database filename
        self.DBSession = sessionmaker(bind=self.engine)

        #Create a session
        self.session = self.DBSession()

        self._observers = []


    def attach(self, observer):
        """adding observer"""
        self._observers.append(observer)

    def _update_observers(self):
        """activate observer"""
        for obs in self._observers:
            obs()


    def get_sequence_num(self):
        """ Getter for sequence number """  
        return self._last_sequence_num
    
    def get_sensor_model(self):
        """ Returns the name of the sensor (from the sensor reading data) """
        if len(self._sensor_readings) > 0:
            return self._sensor_readings[0].get_sensor_model()

        return None

    def get_time_period(self):
        """ Returns the start and end period of the sensor readings """

        start_time = None
        end_time = None
        if len(self._sensor_readings) > 0:
            start_time = self._sensor_readings[0].get_timestamp()
            end_time = self._sensor_readings[-1].get_timestamp()
            return TimeRange(start_time, end_time)
            
        return None

    def get_reading_stats(self):
        """ Returns the temperature stats - low, avg, high, largest range """

        if len(self._sensor_readings) == 0:
            return

        num_ok_readings = 0
        total_temp = 0.0

        lowest_temp = None
        highest_temp = None

        largest_temp_range = 0.0

        for reading in self._sensor_readings:
            # Ignore bad readings
            if reading.is_error():
                continue

            reading_low_temp = reading.get_min_value()
            reading_avg_temp = reading.get_avg_value()
            reading_high_temp = reading.get_max_value()

            if lowest_temp is None:
                lowest_temp = reading_low_temp
            elif reading_low_temp < lowest_temp:
                lowest_temp = reading_low_temp

            if highest_temp is None:
                highest_temp = reading_high_temp
            elif reading_high_temp > highest_temp:
                highest_temp = reading_high_temp

            num_ok_readings += 1
            total_temp += reading_avg_temp

            curr_temp_range = reading_high_temp - reading_low_temp

            if curr_temp_range > largest_temp_range:
                largest_temp_range = curr_temp_range

        average_temp = (total_temp / num_ok_readings)

        return ReadingStats(lowest_temp, average_temp, highest_temp, largest_temp_range)

    def get_error_readings(self):
        """ Returns strings containing error messages for specific readings """

        if len(self._sensor_readings) == 0:
            return None

        error_msgs = []

        for reading in self._sensor_readings:

            if reading.is_error():
                error_msgs.append(reading.get_error_msg())

        return error_msgs


    def add_reading(self, reading):
        """ TODO """
        
        self.session.add(reading)

        self.session.commit()


    def update_reading(self,id, reading):        
        for oreading in self._sensor_readings:  
            if oreading.get_sequence_num() == int(id):
                oid = oreading.get_sequence_num()
                self.session.delete(oreading)
                reading.id = oid
                self.session.add(reading)
                self.session.commit()

    def delete_reading(self, seq_num):
        """delete seq num reading for reading list"""
               
        no_reading = 1
        for reading in self._sensor_readings:            
            if reading.get_sequence_num() == int(seq_num):
                self.session.delete(reading)
                self.session.commit()
                no_reading = 0 
                break
        if no_reading:
            raise AssertionError
            
     

    def get_reading(self, seq_num):
        """get reading from the list"""
        #return self._sensor_readings[next(i for i,v in enumerate(self._sensor_readings) if v.get_sequence_num() == seq_num)]
        for reading in self._sensor_readings:
            if reading.get_sequence_num() == seq_num:
                return reading
                break

    def get_all_readings(self):
        """return all the reading"""
        return self._sensor_readings
        
   

    
    