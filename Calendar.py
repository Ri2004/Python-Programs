# Calendar
import calendar
year = int(input("Enter Year: "))
print(calendar.TextCalendar(firstweekday=6).formatyear(year))