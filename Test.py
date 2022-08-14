from datetime import date
current_date = date.today()
print(current_date)
print("Day: " + str(current_date.day))
print("Month: " + str(current_date.month))
print("Year: " + str(current_date.year))


# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = date.today()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week)