import datetime
import pytz
print('Create now date by passing tz=pytz.UTC')

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
print('We can change the timezone after creating the date using astimezone(timezone)')

dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
print('')


print('We can get all timezone from pytz.all_timezones')
for tz in pytz.all_timezones:
	print(tz)

print('')
print('Convert naive datetime to timezone aware datetime by localizing naive datetime using tz.localize(datetime)')

dt_naive = datetime.datetime.today()
print('Naive datetime: ', dt_naive)
mtn_tz = pytz.timezone('US/Mountain')
dt_naive = mtn_tz.localize(dt_naive)
print('After localizing: ', dt_naive)
