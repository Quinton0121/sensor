class TimeRange:
    """ Data class for the time range, includes formatting of the datetime values """

    def __init__(self, start, end):
        """ Constructor for TimeRange class """

        self._start_timestamp = start
        self._end_timestamp = end

    def get_start_datetime(self, format):
        """ Getter for start time """

        return self._start_timestamp.strftime(format)

    def get_end_datetime(self, format):
        """ Getter for end time """

        return self._end_timestamp.strftime(format)
