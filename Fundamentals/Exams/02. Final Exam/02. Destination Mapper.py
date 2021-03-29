import re


given_string = input()
pattern = r"(/|=)(?P<destination>[A-Z][A-Za-z]{2,})\1"
destinations = []
travel_points = 0
for matches in re.finditer(pattern, given_string):
    destination = matches.group('destination')
    travel_points += len(destination)
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")