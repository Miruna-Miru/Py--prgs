# date and time and calender 
import time
import calendar
print(time.time())
print(time.localtime())
ticks =time.asctime()# asctime is a formated time 
print(ticks)
print(calendar.month(2023,2))
print(calendar.isleap(2022))