import re

pattern = r'(\||#)([A-Za-z\s]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1(\d+)\1'
text = input()
matches = re.findall(pattern, text)
total_calories = sum([int(match[3]) for match in matches])
days = total_calories // 2000  # each day consumes 2000 cal

print(f"You have food to last you for: {days} days!")
for current_food in matches:
    food = current_food[1]
    exp_date = current_food[2]
    calories = current_food[3]
    print(f"Item: {food}, Best before: {exp_date}, Nutrition: {calories}")
