"""
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
"""
import timeit

class Time:

    def __init__(self, hour=-0, minute=0, second=0):
        self.hour = hour
        self.minute = minute 
        self.second = second 

    
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


    def time_to_init(self):
        """ Computes the number of seconds since midnight """ 
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_init() + other.time_to_init()
        return(init_to_time(seconds))
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return init_to_time(seconds)

    def is_valid(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True 


# Intializes time object 
def init_to_time(seconds):
    """ Makes a new time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time 

