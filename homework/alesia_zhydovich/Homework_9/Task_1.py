import datetime


date_time = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(date_time, '%b %d, %Y - %H:%M:%S')
month = python_date.strftime('month: %B')
new_date = python_date.strftime('%d.%m.%Y, %H:%M')

print(month)
print(new_date)
