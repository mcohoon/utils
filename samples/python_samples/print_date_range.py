#!/usr/bin/python

import datetime

# find the range of dates.
#formatting for date: YYY-MM-DD for timedelta

def FormattedDate(dt1, dt2):
    year,month,day = dt1.split("-")
    start_date = datetime.date(int(year),int(month),int(day))

    year,month,day = dt2.split("-")
    end_date = datetime.date(int(year),int(month),int(day))

    diff_date = end_date - start_date 
    days_diff =  diff_date.days
    #returns an int like 350

    current_date = start_date

    for x in range(days_diff):
        current_date = current_date + datetime.timedelta(1)
        print "string123-" + str(current_date)

if __name__ == "__main__":
    dt1 = '2014-01-01'
    dt2 = '2014-12-31' 
    FormattedDate(dt1, dt2)
