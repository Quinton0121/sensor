class ReadingStats:
    """ Data class for reading statistics """

    def __init__(self, min_reading, avg_reading, max_reading, reading_range):
        """ Constructor for ReadingStats class """
        self._min_reading = min_reading
        self._avg_reading = avg_reading
        self._max_reading = max_reading
        self._max_reading_range = reading_range

    def get_min_reading(self):
        """ Getter for minimum reading """
        return self._min_reading

    def get_avg_reading(self):
        """ Getter for average reading """
        return self._avg_reading

    def get_max_reading(self):
        """ Getter for maximum reading """
        return self._max_reading

    def get_max_reading_range(self):
        """ Getter for reading range """
        return self._max_reading_range
