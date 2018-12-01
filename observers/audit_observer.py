from datetime import datetime


class AuditObserver:
    """ Observer for Auditing """

    def __init__(self, sensor):
        """ Initialize the Sensor """
        self._sensor = sensor

    def __call__(self):
        """ Generate the Report """
        self._report()

    def _report(self):
        """ Print the Report """
        print(self._sensor.get_sensor_model() + " Last Read Sequence Number " + str(self._sensor.get_sequence_num()) + " at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
