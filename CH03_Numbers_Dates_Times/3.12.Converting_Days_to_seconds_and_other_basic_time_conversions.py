# @Time: 2022/4/14 17:41
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.12.Converting_Days_to_seconds_and_other_basic_time_conversions.py


from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.total_seconds())


from datetime import datetime
a = datetime(2022, 4, 14)
print(a + timedelta(days=10))

b = datetime(2022, 4, 16)
d = b - a
print(d.days)

now = datetime.now()
print(now)
print(now + timedelta(minutes=30))

#When making calculations, it should be noted that datetime is aware of leap years

from dateutil.relativedelta import relativedelta
a = datetime(2022, 4, 14)
try:
    b = a + timedelta(months=1)
except:
    print("can not use arg months with timedelta")
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    b = datetime(2022, 4, 15)
    d = relativedelta(b, a)
    print(d)
    print(d.months)
    print(d.days)


