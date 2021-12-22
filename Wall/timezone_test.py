# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/22/21
"""
import datetime
import pytz

print('Without pytz:')
dt1 = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
dt2 = dt1.astimezone(datetime.timezone(datetime.timedelta(hours=8)))  # 轉換時區 -> 東八區

print(f"UTC:\t {dt1}")
print(f"UTC+8:\t {dt2}")
print(dt2.strftime("%Y-%m-%d %H:%M:%S"))  # 將時間轉換為 string
print()

# ref: https://blog.pastwind.org/2019/08/pytzdatetime.html
print('With pytz:')
tz = pytz.timezone('Asia/Taipei')
my_time = tz.localize(datetime.datetime.now())

print(my_time, type(my_time))
