# Finding day of the week from date

from datetime import datetime


def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")


print("Task 3: Day of the Week")
print(get_day_of_week("2025-11-04"))
print(get_day_of_week("2023-01-01"))
print(get_day_of_week("2000-12-25"))
