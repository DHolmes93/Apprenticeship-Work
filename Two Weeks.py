import datetime
import calendar
from datetime import timedelta




def two_weeks(all_weeks):
# Enter Date
    date_1 = input("Enter Date\n")
# Date entered is converted into an object
    start_date = datetime.datetime.strptime(date_1, "%Y-%m-%d")
# Date entered is added by 14 days
    two_weeks_from_date = start_date + timedelta(days = 14)

#     previous_date = two_weeks_from_date


    for date in range(all_weeks):
        print(previous_date.strftime("%Y-%m-%d"))
        previous_date = previous_date + timedelta(days=14) 


two_weeks(10)
    

def all_weeks():
    first_date = input("Enter the date\n")
    week_two = first_date + datetime.timedelta(days=14)
    print(week_two)

all_weeks()

    






