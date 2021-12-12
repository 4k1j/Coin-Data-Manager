from enum import Enum


class CandleUnit(Enum):
    MIN_1 = "minutes/1"
    MIN_3 = "minutes/3"
    MIN_5 = "minutes/5"
    MIN_10 = "minutes/10"
    MIN_15 = "minutes/15"
    MIN_30 = "minutes/30"
    MIN_60 = "minutes/60"
    MIN_240 = "minutes/240"
    DAY = "days"
    WEEK = "weeks"
    MONTH = "months"


if __name__ == '__main__':
    print(f"{CandleUnit.MIN_1.value}")