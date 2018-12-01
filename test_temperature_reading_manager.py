from sensors.temperature_sensor_manager import TemperatureSensorManager
from readings.temperature_reading import TemperatureReading
import unittest 
import csv
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open
import inspect
import datetime

class TestTemperatureReadingManager(unittest.TestCase):
    """Unit test for the temperature reading manager"""
    temperature_results = [['2018-09-23 20:04:01.999',1,'ABC Sensor Temp M301A',20.332,21.445,22.013,'OK'],
                            ['2018-09-23 20:04:02.001',11,'ABC Sensor Temp M301A',-50.000,-50.000,-50.000,'LOW_TEMP'],
                            ['2018-09-23 20:05:01.324',12,'ABC Sensor Temp M301A',20.142,21.528,21.803,'OK'],
                            ['2018-09-23 20:06:03.873',13,'ABC Sensor Temp M301A',20.212,21.641,22.017,'OK'],
                            ['2018-09-23 20:07:01.453',14,'ABC Sensor Temp M301A',100.000,100.000,100.000,'HIGH_TEMP'],
                            ['2018-09-23 20:08:00.111',15,'ABC Sensor Temp M301A',21.244,21.355,22.103,'OK'],
                            ['2018-09-23 20:09:02.324',16,'ABC Sensor Temp M301A',21.112,22.345,22.703,'OK'],
                            ['2018-09-23 20:10:02.454',17,'ABC Sensor Temp M301A',20.513,21.745,22.105,'OK'],
                            ['2018-09-23 20:11:01.223',18,'ABC Sensor Temp M301A',20.333,21.348,21.943,'OK'],
                            ['2018-09-23 20:12:00.999',19,'ABC Sensor Temp M301A',20.332,21.445,22.013,'OK'],
                            ['2018-09-23 20:13:01.101',20,'ABC Sensor Temp M301A',19.060,20.001,20.500,'OK'],
                        ]
    
    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """set up default object to test"""
        csv.reader = MagicMock(return_value=TestTemperatureReadingManager.temperature_results) 
        csv.write = MagicMock()          
        self.temperature_reading_manager1= TemperatureSensorManager("../data/temperature_results.csv")
        self.temperature_reading_manager1.load_readings() 
        self.reading = TemperatureReading(datetime.datetime.strptime('2018-09-23 20:04:01.999',"%Y-%m-%d %H:%M:%S.%f"),1,'ABC Sensor Temp M301A',20.332,21.445,22.013,'OK')
        self.temperature_reading_manager_none=TemperatureSensorManager(None)
        
        self.logPoint()

    def tearDown(self):
        """reset sensor object for testing""" 

        self.logPoint()
 
    def logPoint(self):
        """print out a log statement for each use of set up function"""

        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()'%(currentTest, callingFunction))

    def test_create_temperature_reading_manager(self):
        """check the construction create object"""

        self.assertIsInstance(self.temperature_reading_manager1,TemperatureSensorManager,"Must input valid parameters")

    def test_add_reading(self):
        """test method adds reading to the sensor list"""
        total_readings = len(self.temperature_reading_manager1.get_all_readings())
        self.temperature_reading_manager1.add_reading(self.reading)
        self.assertEqual(len(self.temperature_reading_manager1.get_all_readings()),total_readings+1)

    def test_add_reading_none(self):
        """test method reject none type reading"""               
        self.assertRaisesRegex(AttributeError,"'NoneType' object has no attribute 'set_sequence_num'",self.temperature_reading_manager1.add_reading,None)
    
    def test_add_reading_empty(self):
        """test method reject empty  reading"""               
        self.assertRaisesRegex(AttributeError,"'str' object has no attribute 'set_sequence_num'",self.temperature_reading_manager1.add_reading,'')

    def test_update_reading(self):
        """test method update reading from the list"""
        self.temperature_reading_manager1.update_reading(1,TemperatureReading(datetime.datetime.strptime('2018-09-23 20:04:01.999',"%Y-%m-%d %H:%M:%S.%f"),1,'new sensor',20.332,21.445,22.013,'ok'))
        self.assertEqual(self.temperature_reading_manager1.get_sensor_model(),"new sensor")

    def test_update_reading_none(self):
        """test method reject none type reading """
        self.assertRaisesRegex(AttributeError,"'NoneType' object has no attribute 'set_sequence_num'",self.temperature_reading_manager1.update_reading,1,None)
    
    def test_update_reading_empty(self):
        """test method reject none type reading """
        self.assertRaisesRegex(AttributeError,"'str' object has no attribute 'set_sequence_num'",self.temperature_reading_manager1.update_reading,1,'')
    
    def test_update_reading_invalid_seq_num(self):
        """test method reject invalid seq num """
        self.assertRaisesRegex(UnboundLocalError,"local variable 'idx' referenced before assignment",self.temperature_reading_manager1.update_reading,100,TemperatureReading(datetime.datetime.strptime("2018-09-23 20:07","%Y-%m-%d %H:%M"),'new sensor',1,20.332,21.445,22.013,'ok'))
    
    def test_delete_reading(self):
        """test method delete the require reading"""
        total_readings = len(self.temperature_reading_manager1.get_all_readings())
        self.temperature_reading_manager1.delete_reading(1)        
        self.assertEqual(len(self.temperature_reading_manager1.get_all_readings()),total_readings-1)
    
    def test_delete_reading_invalid_seq_num(self):
        """test method reject invalid seq num"""
        self.assertRaisesRegex(AssertionError,"",self.temperature_reading_manager1.delete_reading,100)

    def test_load_readings(self):        
        """test readings load to sensor"""
        self.assertTrue(len(self.temperature_reading_manager1.get_all_readings())>0)

    def test_get_sequence_num(self):
        """test method return the last sequence number"""
        self.assertEqual(self.temperature_reading_manager1.get_sequence_num(),20)
        
    def test_get_sensor_model(self):
        """test method return the sensor model"""
        self.assertEqual(self.temperature_reading_manager1.get_sensor_model(),'ABC Sensor Temp M301A')
    
    def test_get_time_period(self):
        """test method return corret object"""
        self.assertEqual(self.temperature_reading_manager1.get_time_period().get_start_datetime('%Y-%m-%d %H:%M'),'2018-09-23 20:04')
        self.assertEqual(self.temperature_reading_manager1.get_time_period().get_end_datetime('%Y-%m-%d %H:%M'),'2018-09-23 20:13')
        

    def test_get_reading_stats(self):      
        """test method return reading stats object"""
        self.assertEqual(self.temperature_reading_manager1.get_reading_stats().get_min_reading(), 19.06)
        self.assertEqual(self.temperature_reading_manager1.get_reading_stats().get_avg_reading(),21.428111111111107)
        self.assertEqual(self.temperature_reading_manager1.get_reading_stats().get_max_reading(),22.703)
        self.assertEqual(self.temperature_reading_manager1.get_reading_stats().get_max_reading_range(),1.8049999999999997)

    def test_get_error_readings(self):
        """test method return error reading list"""
        self.assertEqual(self.temperature_reading_manager1.get_error_readings()[0],'Low Temperature (-50°C) at 2018/09/23 20:04, Sequence: 11')

    def test_get_reading(self):
        """test method return Reading object"""
        self.assertIsInstance(self.temperature_reading_manager1.get_reading(1),TemperatureReading)


    def test_get_all_readings(self):
        """test all readings are return"""
        self.assertEqual(len(self.temperature_reading_manager1.get_all_readings()),11)

    
if __name__ == '__main__':
   unittest.main()
