# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.


age = int(input("What is your current age? "))

years_will_live = 90
month_in_a_year = 12
week_in_a_year = 52
days_in_a_year = 365

years_remaining = years_will_live - age
month_remaining = years_remaining * month_in_a_year
week_remaining = years_remaining * week_in_a_year
days_remaining = years_remaining * days_in_a_year

print(f"You have {days_remaining} days, {week_remaining} weeks, and {month_remaining} months left.")


