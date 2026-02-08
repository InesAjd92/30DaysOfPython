### Day 16 : Date and time in Python ###

## Exercises ##

# first of all, I import the module datetime

from datetime import datetime

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
print(now)

day = now.day
print(day)

month = now.month
print(month) #feb

year = now.year
print(year) #2026

hour =  now.hour
minute = now.minute
timestamp = now.timestamp()

print(hour, minute, timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

# I need strftime 

now = datetime.now() # date to change
t = now.strftime("%m/%d/%Y, %H:%M:%S") # format code
print(t)

# 3. Today is 5 December, 2019. Change this time string to time.

time_str = "5 December, 2019"
date_object = datetime.strptime(time_str, "%d %B, %Y")
print(date_object)

# 4. Calculate the time difference between now and new year.

new_year_2026 = datetime(year= 2026, month=1, day=1)
diff_new_year = now - new_year_2026
print(diff_new_year)

time_stamp_date = datetime(year= 1970, month=1, day=1)
diff_time_stamp = now - time_stamp_date
print(diff_time_stamp)

# 6. Think, what can you use the datetime module for? Examples:

# With this module, maybe i can filter from year, i can clear data
