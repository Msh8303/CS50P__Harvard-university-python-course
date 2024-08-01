from datetime import date

# Get today's date
t = date.today()

# Convert the date object to a string in the format "yyyy-mm-dd"
date_string = str(t)

# Split the date string using "-" as the delimiter
y, m, d = map(int, date_string.split("-"))

print(y, m, d)
