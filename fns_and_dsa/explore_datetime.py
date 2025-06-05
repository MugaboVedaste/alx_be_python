import datetime
from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ", current_date)
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    furture_date =  current_date + timedelta(days = number_of_days)
    print("Future date: ", furture_date.strftime("%Y-%m-%d"))
display_current_datetime()
