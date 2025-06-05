import datetime
from datetime import datetime, timedelta

current_date = datetime.now() 
current_date1 = current_date.strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime():
    print("Current date and time: ", current_date1)
    

    

def calculate_future_date():
    display_current_datetime()
    
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    furture_date =  current_date + timedelta(days = number_of_days)
    print("Future date: ", furture_date.strftime("%Y-%m-%d"))
calculate_future_date()
