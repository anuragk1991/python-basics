import datetime
import calendar

balance = 5000
interest_rate = 0.13
monthly_payment = 500

today = datetime.datetime.today()

days = calendar.monthrange(today.year, today.month)[1]
days_remaining_in_month = days - today.day
start_date = today + datetime.timedelta(days_remaining_in_month+1)


while(balance > 0):
	interest = balance * interest_rate/12
	balance += interest
	balance -= monthly_payment

	print('Date: {}'.format(start_date.date()))

	start_date = start_date + datetime.timedelta(calendar.monthrange(start_date.year, start_date.month)[1])
	balance = 0 if balance < 0 else round(balance, 2)
	print('Balance: {}'.format(balance))


print('')
current_wt = 220
goal_wt = 180
wt_reduce_per_week = 2
print('Current Weight: {} lbs'.format(current_wt))
print('Goal Weight: {} lbs'.format(goal_wt))
print('Weight reduced per week: {} lbs'.format(wt_reduce_per_week))


start_date = datetime.date.today()
end_date = start_date
print('Start Date: {}'.format(start_date))

while current_wt > goal_wt:
	end_date = end_date + datetime.timedelta(days=7)
	current_wt -= wt_reduce_per_week

print('End Date: {}'.format(end_date))
diff = end_date - start_date
print('Goal reached in {} weeks'.format(diff.days//7))