#<20241211>

#calendar
import calendar
calendar.prcal(2024)
calendar.prmonth(2024,1)
print(calendar.weekday(2024,12,15))
print()

#오늘의 요일
import datetime

days = ['월', '화', '수', '목', '금', '토', '일']
weekday = datetime.date.today().weekday()
print(weekday)
print('오늘은' + days[weekday] + '요일')

weekday = datetime.date(2025, 12, 25).weekday()
print('크리스마스는' +days[weekday]+'요일')

