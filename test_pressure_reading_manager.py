from sensors.pressure_sensor_manager import PressureSensorManager
from readings.pressure_reading import PressureReading
import unittest 
import csv
from unittest.mock import MagicMock
from unittest.mock import patch,mock_open
import inspect
import datetime

class TestPressureReadingManager(unittest.TestCase):
    """Unit test for the pressure reading manager"""   
    pressure_results = [['2018-09-23 19:56','ABC Sensor Pres M100',1,50.163,51.435,52.103,'GOOD'],
                        ['2018-09-23 19:58','ABC Sensor Pres M100',3,50.142,51.528,51.803,'GOOD'],
                        ['2018-09-23 19:57','ABC Sensor Pres M100',2,50.163,51.435,53.103,'GOOD'],
                        ['2018-09-23 19:59','ABC Sensor Pres M100',4,50.212,51.641,55.017,'GOOD'],
                        ['2018-09-23 20:00','ABC Sensor Pres M100',5,100.000,100.000,100.000,'HIGH_PRESSURE'],
                        ['2018-09-23 20:01','ABC Sensor Pres M100',6,51.244,51.355,52.103,'GOOD'],
                        ['2018-09-23 20:02','ABC Sensor Pres M100',7,51.112,52.345,52.703,'GOOD'],
                        ['2018-09-23 20:03','ABC Sensor Pres M100',8,50.513,51.745,53.105,'GOOD'],
                        ['2018-09-23 20:04','ABC Sensor Pres M100',9,50.333,51.348,51.943,'GOOD'],
                        ['2018-09-23 20:05','ABC Sensor Pres M100',10,50.332,51.445,52.013,'GOOD'],
                        ['2018-09-23 20:06','ABC Sensor Pres M100',11,0.000,0.000,0.000,'LOW_PRESSURE']
                        ]
    
    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """set up default object to test"""
        csv.reader = MagicMock(return_value=TestPressureReadingManager.pressure_results) 
        csv.write = MagicMock()          
        self.pressure_reading_manager1= PressureSensorManager("../data/pressure_results.csv")
        self.pressure_reading = PressureReading(datetime.datetime.strptime("2018-09-23 20:07","%Y-%m-%d %H:%M"),"ABC Sensor Pres M100",1,50.332,51.445,52.013,"HIGH_PRESSURE")
        self.pressure_reading_manager1.load_readings()        
        self.logPoint()

    def tearDown(self):
        """reset sensor object for testing""" 
        self.logPoint()
 
    def logPoint(self):
        """print out a log statement for each use of set up function"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()'%(currentTest, callingFunction))

    def test_create_pressure_reading_manager(self):
        """check the construction create object"""
        self.assertIsNotNone(self.pressure_reading_manager1)

    def test_add_reading(self):
        """test method adds reading to the sensor list"""
        total_readings = len(self.pressure_reading_manager1.get_all_readings())
        self.pressure_reading_manager1.add_reading(self.pressure_reading)
        self.assertEqual(len(self.pressure_reading_manager1.get_all_readings()),total_readings+1)

    def test_add_reading_none(self):
        """test method reject none type reading"""               
        self.assertRaisesRegex(AttributeError,"'NoneType' object has no attribute 'set_sequence_num'",self.pressure_reading_manager1.add_reading,None)
    
    def test_add_reading_empty(self):
        """test method reject empty reading"""               
        self.assertRaisesRegex(AttributeError,"'str' object has no attribute 'set_sequence_num'",self.pressure_reading_manager1.add_reading,'')

    def test_update_reading(self):
        """test method update reading from the list"""
        self.pressure_reading_manager1.update_reading(1,PressureReading(datetime.datetime.strptime("2018-09-23 20:07","%Y-%m-%d %H:%M"),'new sensor',1,20.332,21.445,22.013,'ok'))
        self.assertEqual(self.pressure_reading_manager1.get_sensor_model(),"new sensor")

    def test_update_reading_none(self):
        """test method reject none type reading """
        self.assertRaisesRegex(AttributeError,"'NoneType' object has no attribute 'set_sequence_num'",self.pressure_reading_manager1.update_reading,1,None)
    
    def test_update_reading_empty(self):
        """test method reject none type reading """
        self.assertRaisesRegex(AttributeError,"'str' object has no attribute 'set_sequence_num'",self.pressure_reading_manager1.update_reading,1,'')
    
    def test_update_reading_invalid_seq_num(self):
        """test method reject invalid seq num """
        self.assertRaisesRegex(UnboundLocalError,"local variable 'idx' referenced before assignment",self.pressure_reading_manager1.update_reading,100,PressureReading(datetime.datetime.strptime("2018-09-23 20:07","%Y-%m-%d %H:%M"),'new sensor',1,20.332,21.445,22.013,'ok'))
    


    def test_delete_reading(self):
        """test method delete the require reading"""
        total_readings = len(self.pressure_reading_manager1.get_all_readings())
        self.pressure_reading_manager1.delete_reading(1)        
        self.assertEqual(len(self.pressure_reading_manager1.get_all_readings()),total_readings-1)

    def test_delete_reading_invalid_seq_num(self):
        """test method reject invalid seq num"""
        self.assertRaisesRegex(AssertionError,"",self.pressure_reading_manager1.delete_reading,100)


    def test_load_readings(self):     
        """test readings load to sensor"""
        self.assertTrue(len(self.pressure_reading_manager1.get_all_readings())>0)

    def test_get_sequence_num(self):        
        """test method return the last sequence number"""
        self.assertEqual(self.pressure_reading_manager1.get_sequence_num(),11)
        
    def test_get_sensor_model(self):       
        """test method return the sensor model"""
        self.assertEqual(self.pressure_reading_manager1.get_sensor_model(),'ABC Sensor Pres M100')
    
    def test_get_time_period(self):
        """test method return corret object"""
        self.assertEqual(self.pressure_reading_manager1.get_time_period().get_start_datetime('%Y-%m-%d %H:%M'),'2018-09-23 19:56')
        self.assertEqual(self.pressure_reading_manager1.get_time_period().get_end_datetime('%Y-%m-%d %H:%M'),'2018-09-23 20:06')
        

    def test_get_reading_stats(self):        
        """test method return reading stats object"""
        self.assertEqual(self.pressure_reading_manager1.get_reading_stats().get_min_reading(),50.142)
        self.assertEqual(self.pressure_reading_manager1.get_reading_stats().get_avg_reading(),51.60525)
        self.assertEqual(self.pressure_reading_manager1.get_reading_stats().get_max_reading(),55.017)
        self.assertEqual(self.pressure_reading_manager1.get_reading_stats().get_max_reading_range(),4.805)

    def test_get_error_readings(self):
        """test method return error reading list"""
        self.assertEqual(self.pressure_reading_manager1.get_error_readings()[0],'High Pressure (100 kPA) at 2018/09/23 20:00, Sequence: 5')

    def test_get_reading(self):
        """test method return Reading object"""
        self.assertIsInstance(self.pressure_reading_manager1.get_reading(1),PressureReading)

    def test_get_all_readings(self):
        """test all readings are return"""
        self.assertEqual(len(self.pressure_reading_manager1.get_all_readings()),10)
    
    
if __name__ == '__main__':
   unittest.main()
