class PressureObserver:
    """ Pressure Sensor Observer """

    DATE_FORMAT = '%Y/%m/%d %H:%M'

    def __init__(self, pressure_sensor):
        """ Initialize the Pressure Sensor """

        if pressure_sensor is None:
            raise ValueError("Pressure Sensor should not be None")

        self._sensor = pressure_sensor

    def __call__(self):
        """ Generate the Pressure Sensor Report """
        self._pressure_report()

    def _pressure_report(self):
        """ Print the Report """

        sensor_name = self._sensor.get_sensor_model()

        if sensor_name is not None:
            print("Sensor: %s" % (sensor_name))
        else:
            print("No Sensor Results")

        time_period = self._sensor.get_time_period()
        time_start = time_period.get_start_datetime(PressureObserver.DATE_FORMAT)
        time_end = time_period.get_end_datetime(PressureObserver.DATE_FORMAT)

        if time_start is not None and time_end is not None:
            print("Period: %s to %s" % (time_start, time_end))
        else:
            print("No Results")

        stats = self._sensor.get_reading_stats()

        print("Lowest Pressure: %f kPa" % (stats.get_min_reading()))
        print("Average Pressure: %0.5f kPa" % (stats.get_avg_reading()))
        print("Highest Pressure: %f kPa" % (stats.get_max_reading()))
        print("Largest Pressure Range: %f kPa" % (stats.get_max_reading_range()))

        error_msgs = self._sensor.get_error_readings()
        if len(error_msgs) > 0:
            print("Error Messages:")
            for msg in error_msgs:
                print("  " + msg)
