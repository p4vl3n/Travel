volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours_away = float(input())
pipe_one_volume = pipe_one_debit * hours_away
pipe_two_volume = pipe_two_debit * hours_away
filled_volume = pipe_one_volume + pipe_two_volume
pipe_one_percentage = pipe_one_volume / filled_volume * 100
pipe_two_percentage = pipe_two_volume / filled_volume * 100
percentage_full = (pipe_one_volume + pipe_two_volume) / volume * 100
if filled_volume <= volume:
    print(f"The pool is {percentage_full:.2f}% full. Pipe 1: {pipe_one_percentage:.2f}%. Pipe 2: {pipe_two_percentage:.2f}%.")
else:
    overflow = filled_volume - volume
    print(f"For {hours_away} hours the pool overflows with {overflow:.2f} liters.")
