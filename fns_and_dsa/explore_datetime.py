from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("YYYY-MM-DD HH:MM:SS"))

def calculate_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    print(future_date.strftime("YYYY-MM-DD"))



days_to_add = int(input("Enter number of days to add to the curent date: "))
display_current_datetime()
calculate_future_date(days_to_add)

