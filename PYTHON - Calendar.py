import calendar

def show_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

# Replace these values with the desired year and month
year_input = 2023
month_input = 12

show_calendar(year_input, month_input)


