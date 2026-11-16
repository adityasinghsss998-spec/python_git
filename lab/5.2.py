# Task 2: Using datetime to get day of week

from datetime import datetime


def get_day_of_week(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."


# Testing
print("Day of week for 2025-11-11:", get_day_of_week("2025-11-11"))
print("Day of week for 2000-01-01:", get_day_of_week("2000-01-01"))
