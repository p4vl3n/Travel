movie_type = input()
rows = int(input())
columns = int(input())
price = 0
if movie_type == "Premiere":
    price = 12
elif movie_type == "Normal":
    price = 7.50
elif movie_type == "Discount":
    price = 5
full_capacity = rows * columns
revenue = full_capacity * price
print(f'{revenue:.2f} leva')