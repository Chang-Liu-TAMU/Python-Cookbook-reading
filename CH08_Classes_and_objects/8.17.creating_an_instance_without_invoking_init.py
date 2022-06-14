class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date.__new__(Date)
print(d)
try:
    print(d.year)
except Exception as e:
    print(e)

data = {'year':2012, 'month':8, 'day':29}
for key, value in data.items():
    setattr(d, key, value)
print(d.year)

#####################################\
from time import localtime
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

'''
When creating instances in a nonstandard way, it’s usually best to not make too many
assumptions about their implementation. As such, you generally don’t want to write
code that directly manipulates the underlying instance dictionary __dict__ unless you
know it’s guaranteed to be defined. Otherwise, the code will break if the class uses
__slots__, properties, descriptors, or other advanced techniques.
'''