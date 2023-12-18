Create a python script that show a calendar 

ChatGPT
Certainly! Here's a simple Python script using the calendar module to display a calendar for a given year and month:

python
Copy code
import calendar

def show_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

# Replace these values with the desired year and month
year_input = 2023
month_input = 12

show_calendar(year_input, month_input)
Replace the year_input and month_input variables with the desired year and month you want to display the calendar for. When you run this script, it will print the calendar for the specified year and month.








