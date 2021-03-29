deposit = float(input())
period = float(input())
yearly_interest = float(input()) / 100
total_interest = float(deposit * yearly_interest)
monthly_interest = float(total_interest / 12)
amount_at_the_end = deposit + period * monthly_interest
print(amount_at_the_end)