"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

date_info = input("enter input in the following format: '14_cal.py month [year]': ")

date_info_list = date_info.split(' ')

if len(date_info_list) == 0:
    print(calendar.month(datetime.now().year, datetime.now().month))
elif len(date_info_list) == 1:
    print(calendar.month(2020, int(date_info_list[0])))
elif len(date_info_list) == 2:
    print(calendar.month(int(date_info_list[1]), int(date_info_list[0])))
else:
    print("Invalid format. Should be: '14_cal.py month [year]'")