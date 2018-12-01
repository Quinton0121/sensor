class TempObserver:
    """ Temperature Sensor Observer """

    DEGREE_SIGN = u'\N{DEGREE SIGN}'
    DATE_FORMAT = '%Y/%m/%d %H:%M'

    def __init__(self, temp_sensor):
        """ Initialize the Pressure Sensor """

        if temp_sensor is None:
            raise ValueError("Pressure Sensor should not be None")

        self._sensor = temp_sensor

    def __call__(self):
        """ Generate the Report """

        self._temperature_report()

    def _temperature_report(self):
        """ Print the Report """

        sensor_name = self._sensor.get_sensor_model()

        if sensor_name is not None:
            print("Sensor: %s" % (sensor_name))
        else:
            print("No Sensor Results")

        time_period = self._sensor.get_time_period()
        time_start = time_period.get_start_datetime(TempObserver.DATE_FORMAT)
        time_end = time_period.get_end_datetime(TempObserver.DATE_FORMAT)

        if time_start is not None and time_end is not None:
            print("Period: %s to %s" % (time_start, time_end))
        else:
            print("No Results")

        stats = self._sensor.get_reading_stats()

        print("Lowest Temp: %f%cC" % (stats.get_min_reading(), TempObserver.DEGREE_SIGN))
        print("Average Temp: %0.5f%cC" % (stats.get_avg_reading(), TempObserver.DEGREE_SIGN))
        print("Highest Temp: %f%cC" % (stats.get_max_reading(), TempObserver.DEGREE_SIGN))
        print("Largest Temp Range: %f%cC" % (stats.get_max_reading_range(), TempObserver.DEGREE_SIGN))

        error_msgs = self._sensor.get_error_readings()
        if len(error_msgs) > 0:
            print("Error Messages:")
            for msg in error_msgs:
                print("  " + msg)
