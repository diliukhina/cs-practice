import sys
from stats import read_valid, average_by_city, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
errors = sum(1 for line in lines if line.strip()) - len(records)
print(len(records))
print(errors)
if records:
    city = warmest_city(records)
    print(f"{average_by_city(records)[city]:.1f}")
else:
    print("0.0")
