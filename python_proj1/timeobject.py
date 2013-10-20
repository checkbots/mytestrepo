""" Sekhar: This module has code to implement a 'Time' object. We are
    using this and associated test_timeobject module to demonstrate writing
    simple (no boiler plate) tests with py.test and to demonstrate doctest
    format tests.
"""


# Implement a time object.
class Time(object):
    """Represents the time of the day.
    Attributes: hour,minute,second
    >>> t = Time(2,10,15)
    >>> print t
    02:10:15
    >>> t = Time(2,10)
    >>> print t
    02:10:00
    >>> t = Time(2)
    >>> print t
    02:00:00
    >>> t = Time()
    >>> print t
    00:00:00
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute \
                and self.second == other.second:
            return True
        return False

    def time_to_int(self):
        """Return number of seconds from a time object
        >>> t = Time(2,10,15)
        >>> t.time_to_int()
        7815
        """
        return self.hour * 3600 + self.minute * 60 + self.second

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        return int_to_time(self.time_to_int() + seconds)

    def valid_time(self):
        """Check if a given time object is valid
        >>> t = Time(25,10,59)
        >>> t.valid_time()
        True
        >>> t = Time(1,100)
        >>> t.valid_time()
        False
        >>> t = Time(1,10,60)
        >>> t.valid_time()
        False
        """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

    def __add__(self, other):
        """Add time or number (seconds) to a time object
        >>> t1 = Time(1,10,10)
        >>> t2 = Time(2,20,20)
        >>> print t1 + t2
        03:30:30
        >>> print t1 + 30
        01:10:40
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)


def int_to_time(seconds):
    """Convert integer (number of seconds) to a time object
    >>> print int_to_time(100)
    00:01:40
    >>> print int_to_time(1000)
    00:16:40
    >>> print int_to_time(10000)
    02:46:40
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
