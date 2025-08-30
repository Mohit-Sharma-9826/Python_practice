import datetime as dt

date =dt.datetime.now() # type => datetime.datetime
year = date.year        # type => int
month = date.month      # type => int
day = date.day          # type => int

day_of_week = date.weekday()   # 0 for Monday ad go upto 6 which is Sunday.
date_value = date.date()       # type => datetime.date

# print(date_value)
# print(type(date_value))

date2 = dt.datetime(year=2006, month=4, day=8, hour=11, minute=25, second=45, microsecond=452)
print(date2)

date3 = dt.datetime(2024, 12, 26)
print(date3)
