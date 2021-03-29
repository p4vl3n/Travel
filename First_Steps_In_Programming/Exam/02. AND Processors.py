from math import floor
processors_to_be_made = int(input())
workers = int(input())
working_days = int(input())
processor_cost = 110.10
actual_made = floor(workers * 8 * working_days / 3)
expected_revenue = processors_to_be_made * processor_cost
actual_revenue = actual_made * processor_cost
difference = abs(expected_revenue - actual_revenue)
if actual_revenue >= expected_revenue:
    print(f"Profit: -> {difference:.2f} BGN")
else:
    print(f"Losses: -> {difference:.2f} BGN")