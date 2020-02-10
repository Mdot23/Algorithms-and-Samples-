import timeit


class Time:

    def __init__(self, hour=-0, minute=0, second=0):
        self.hour = hour
        self.minute = minute 
        self.second = second 

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def init_to_time(seconds):

    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time 

    def time_to_int(self):
        minutes = time.hour * 60 + self.minute 
        seconds = minutes * 60 + self.second 
        return seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_init() + other.time_to_int()
        return int_to_time(seconds)
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds) 



