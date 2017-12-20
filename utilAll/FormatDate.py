import datetime


def getYearQuarter(year,quarter):
    if year is None:
        year = datetime.datetime.now().year
    if quarter is None:
        month = datetime.datetime.now().month
        if month in [1, 2, 3]:
            quarter = 1
        elif month in [4, 5, 6]:
            quarter = 2
        elif month in [7, 8, 9]:
            quarter = 3
        else:
            quarter = 4
    return [year,quarter]