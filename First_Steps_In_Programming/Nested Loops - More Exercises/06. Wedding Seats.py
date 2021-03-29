last_sector = input()
rows_in_sector_A = int(input())
seats_in_odd_row = int(input())
seats_in_even_row = seats_in_odd_row + 2
total_seats = 0
for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_in_sector_A + 1):
        if row % 2 != 0:
            for seat in range(97, 97 + seats_in_odd_row):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
        elif row % 2 == 0:
            for seat in range(97, 97 + seats_in_even_row):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
    rows_in_sector_A += 1
print(total_seats)