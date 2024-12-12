# Sharath Chandra Reddy Dumpali -- 00864049
# Create a dictionary of the months and their corresponding number of days
months_dict = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# Use dictionary comprehension to create dictionaries for months with less than 30 days, 31 days, and 30 days
# Months with less than 30 days
less_than_30_days = {month: days for month, days in months_dict.items() if days < 30}
# Months with 31 days
thirtyone_days = {month: days for month, days in months_dict.items() if days == 31}
#  Months with 30 days
thirty_days = {month: days for month, days in months_dict.items() if days == 30}

# Iterating over the dictionary and printing the months with the same first letter
first_letter_dict = {}
for month in months_dict:
    first_letter = month[0]
    if first_letter not in first_letter_dict:
        first_letter_dict[first_letter] = [month]
    else:
        first_letter_dict[first_letter].append(month)

# Iterating over the dictionary and printing the months with the same last letter
last_letter_dict = {}
for month in months_dict:
    last_letter = month[-1]
    if last_letter not in last_letter_dict:
        last_letter_dict[last_letter] = [month]
    else:
        last_letter_dict[last_letter].append(month)

# Using dictionary comprehension to create dictionaries of the months for each season Spring,Fall,Summer,Winter
spring_months = {month: days for month, days in months_dict.items() if month in ['March', 'April', 'May']}
summer_months = {month: days for month, days in months_dict.items() if month in ['June', 'July', 'August']}
fall_months = {month: days for month, days in months_dict.items() if month in ['September', 'October', 'November']}
winter_months = {month: days for month, days in months_dict.items() if month in ['December', 'January', 'February']}

# Printing the outputs with f string format
print(f"Months with less than 30 days: {less_than_30_days}")
print(f"\nMonths with 31 days: {thirtyone_days}")
print(f"\nMonths with 30 days: {thirty_days}")
print(f"\nMonths with the same first letter: {first_letter_dict}")
print(f"\nMonths with the same last letter: {last_letter_dict}")
print(f"\nSpring months: {spring_months}")
print(f"\nSummer months: {summer_months}")
print(f"\nFall months: {fall_months}")
print(f"\nWinter months: {winter_months}")
