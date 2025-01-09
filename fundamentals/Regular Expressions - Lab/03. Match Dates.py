import re

pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'

data = input()

match = re.findall(pattern, data)

for date in match:  # date (dd/mmm/yyyy) are represented as tuples in this case
    day = date[0]
    month = date[2]  # second index because the first index is the separator
    year = date[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')
