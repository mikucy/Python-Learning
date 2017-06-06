import re
from datetime import datetime, timezone, timedelta

# This code convert the input datetime and timezone to timestamp.
def to_timestamp(dt_str, tz_str):
  dt = re.match(r'\d{4}\-\d{1,2}\-\d{1,2}\s\d{1,2}\:\d{1,2}\:\d{1,2}', dt_str).group(0)
  tz = re.match(r'(UTC)([\+\-])(\d{1,2})(\:00)', tz_str).groups()
  if tz[1] == '-':
      tzinfo = int(tz[2]) * -1
  else:
      tzinfo = int(tz[2])
  day = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
  tz_utc = timezone(timedelta(hours=tzinfo))
  time = day.replace(tzinfo=tz_utc)
  return time.timestamp()

# Test
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
