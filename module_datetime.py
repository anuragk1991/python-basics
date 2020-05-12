import datetime
from pprint import pprint


print('datetime.date')
print('Create date object from datetime suing datetime.date(Y, m, d)')

date = datetime.date(2016, 7, 12)
print(date)

print('date object has various properties like day, month, year (date.year, date.month)')
print('Year: ', date.year)
print('Month: ',date.month)
print('Day: ',date.day)


print('We can get today\'s date using datetime.date.today()')
tday = datetime.date.today()
print(tday)

print('')
print('Time Delta')
tdelta = datetime.timedelta(days=7)
bday = datetime.date(2020, 10, 9)
tdelta = bday - tday
print(type(tdelta))


print('datetime.time(h, m, s, ms)')
t = datetime.time(7, 30, 34, 100000)
print(t)

print('')
print('Similarly we can get hour, minute, seconds and miliseconds from time')
print('Hour: ', t.hour)
print('Minute: ', t.minute)
print('Seconds: ', t.second)

print('')
print('datetime.datetime')
print('It contains info about both date and time')
print('datetime.datetime(Y, m, d, h,m,s,ss)')

dtime = datetime.datetime(2019, 8, 20, 12, 8, 29, 100000)
print(dtime)
print('')

print('We van access date, time, day, etc')
print('Day: ', dtime.day)
print('Year: ', dtime.year)
print('')

print('datetime.datetime.today(), datetime.datetime.now(), datetime.datetime.utcnow()')

print('Difference b/w today and now is we can specify timezone in now')
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print('Today: ', dt_today)
print('Now: ', dt_now)
print('UTC Now: ', dt_utcnow)
