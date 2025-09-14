import calendar
from datetime import datetime

def show_calendar(year, month):
    """Show a specific month's calendar."""
    cal = calendar.month(year, month)
    print(cal)

def show_year_calendar(year):
    """Show the full year calendar."""
    cal = calendar.calendar(year)
    print(cal)

def is_leap_year(year):
    """Check if a year is a leap year."""
    return calendar.isleap(year)

def weekday_of_date(year, month, day):
    """Return the weekday name of a given date."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = calendar.weekday(year, month, day)
    return days[day_index]

def next_month(year, month):
    """Return the year and month of the next month."""
    if month == 12:
        return year + 1, 1
    return year, month + 1

def prev_month(year, month):
    """Return the year and month of the previous month."""
    if month == 1:
        return year - 1, 12
    return year, month - 1

# Example usage
year_input = 2023
month_input = 12

print("Selected month:")
show_calendar(year_input, month_input)

print("\nFull year:")
show_year_calendar(year_input)

print(f"\nIs {year_input} a leap year? {is_leap_year(year_input)}")

print("\nWeekday of 2023-12-25:", weekday_of_date(2023, 12, 25))

ny, nm = next_month(year_input, month_input)
print(f"\nNext month: {ny}-{nm}")
py, pm = prev_month(year_input, month_input)
print(f"Previous month: {py}-{pm}")
