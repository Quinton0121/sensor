from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sensors.time_range import TimeRange
from sensors.reading_stats import ReadingStats
from readings.abstract_reading import AbstractReading
from sqlalchemy.pool import SingletonThreadPool
import sqlite3


class AbstractSensorManager:
    """ Abstract Implementation of a Sensor """

    def __init__(self,reader):
        """ Initializes the list of sensor readings for the sensor """

        #Engine - allows the session to etablishes the connection to the DB
        self.engine = create_engine("sqlite:///readings.sqlite") 
        #conn = sqlite3.connect('sqlite:///readings.sqlite', check_same_thread=False)

        #DB Session Maker given a SQLite database filename
        self.DBSession = sessionmaker(bind=self.engine)

        self.session = self.DBSession()

        self.reader = reader

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
        self._last_sequence_num = 0
        for reading in self.session.query(self.reader).all():
            if reading.get_sequence_num() > self._last_sequence_num:
                self._last_sequence_num = reading.get_sequence_num()
        return self._last_sequence_num
    
    def get_sensor_model(self):
        """ Returns the name of the sensor (from the sensor reading data) """
        if len(self._sensor_readings) > 0:
            return self._sensor_readings[0].get_sensor_model()

        return None

    

   


    def add_reading(self, reading):
        """ TODO """
        self.session.add(reading)
        try:
            self.session.commit()
        except:
            self.session.rollback()


    def update_reading(self,iid, reading): 
        ret = self.session.query(self.reader).filter(self.reader.id==iid).first()
        
        
        oid = ret.get_sequence_num()
        self.session.delete(ret)
        reading.id = oid
        self.session.add(reading)
        self.session.commit()
        self.session.close()

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
        
        ret = self.session.query(self.reader).filter(self.reader.id==seq_num).first()
        self.session.close()
        return ret
     

    
        

    def get_all_readings(self):
        """return all the reading"""
        ret = self.session.query(self.reader).all()
        self.session.close()
        return ret
        
        
   

    
    