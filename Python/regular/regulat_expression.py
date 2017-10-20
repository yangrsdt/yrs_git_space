#!/usr/bin/python
# coding = utf8

# import re
#
# print("请输入")
# test = input()
# if re.match(r"[0-9a-zA-Z\_]+",test):
#     print("发邮件")
# else:
#     print("格式错误")

from datetime import datetime,timedelta,timezone
import re

def to_stamp(str,utc_str):
    t = datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
    r = re.compile(r"^UTC([\+|\-])(\d{1,2}):(\d{2})$")
    utc_re = r.match(utc_str)
    Utc = timezone(timedelta(hours=int(utc_re.group(2))))
    print(utc_re.group(2))
    t = t.replace(tzinfo=Utc)
    timestamp = t.timestamp()
    print(timestamp)

to_stamp('2015-6-1 08:10:30','UTC+7:00')

# import re
# from datetime import datetime, timezone, timedelta
#
# def to_timestamp(dt_str, tz_str):
#     m = re.match(r'^UTC([+-]\d{1,2}):(\d{2})$', tz_str)
#     print(m.group(1))
#     tz_utc = timezone(timedelta(hours=int(m.group(1))))
#     dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#     dt = dt.replace(tzinfo=tz_utc)
#     return dt.timestamp()
#
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
#
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# print('Pass')