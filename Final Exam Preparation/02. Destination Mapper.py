import re

pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
text = input()
matches = re.findall(pattern, text)  

destinations = [match[1] for match in matches]
travel_points = sum(len(destination) for destination in destinations)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
