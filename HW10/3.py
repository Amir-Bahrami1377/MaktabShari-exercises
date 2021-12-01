import argparse
from datetime import datetime
import jdatetime

parser = argparse.ArgumentParser(description="Time")
parser.add_argument('-e', '--Early', help='Early history', type=str)
parser.add_argument('-s', '--Second', help='Second history', type=str)
parser.add_argument('-j', '--jalali', help='date format: jalali ', action='store_true')
parser.add_argument('-k', '--leap_year', help='leap year ', action='store_true')
args = parser.parse_args()


def convert_datetime(from_date, to_date):
    return datetime.strptime(from_date, "%Y-%m-%d.%H:%M:%S"), datetime.strptime(to_date, "%Y-%m-%d.%H:%M:%S")


def jalali(date):
    a = jdatetime.date.fromgregorian(date=date.date())
    return date.replace(a.year, a.month, a.day)


def leap_year(date) -> bool:
    a = jdatetime.date.fromgregorian(date=date.date())
    if ((a.year + 38) * 31) % 128 < 30:
        return True
    else:
        return False


x, y = convert_datetime(args.Early, args.Second)
print((y - x).total_seconds())

if args.leapـyear is not False:
    num: int = 0
    start = x
    while x.year < y.year:
        if leap_year(x): num += 1
        x = x.replace(x.year + 1)
    print(f"leap year={num}")
    a=(y - start) / 182
    if a.days >0:
        print(f"time change counter= {a.days}")
    else:
        print(f"no time changes")

if args.jalali is not False:
    x, y = jalali(x), jalali(y)
    print(x, y)
