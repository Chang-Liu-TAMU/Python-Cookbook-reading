# @Time: 2022/4/21 14:45
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.13.Determining_last_friday_date.py

from datetime import datetime, timedelta
from typing import Optional

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]


def get_previous_buday(dayname, start_date: Optional[datetime] = None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(datetime.today())
print(get_previous_buday("Monday"))
print(get_previous_buday("Friday"))

print(get_previous_buday("Thursday", datetime(2022, 4, 22)))


from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

print(d + relativedelta(weekday=FR))

print(d + relativedelta(weekday=FR(-1)))