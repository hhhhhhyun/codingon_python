#datetime 모듈
import datetime
now = datetime.datetime.today()

print(now)
print(now.year, now.month)

print(f"{now.hour}시, {now.minute}분, {now.second}초")
print()

# 지나온 날짜 계산하기
print("지금까지 몇 일?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)

passed_time = today - first_day
print(passed_time)
print(f'개강 이후 {passed_time.days}일 지났습니다.')