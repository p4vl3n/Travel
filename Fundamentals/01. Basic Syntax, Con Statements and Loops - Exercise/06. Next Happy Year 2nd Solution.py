year = int(input())
happy_year = True

while True:
    year_as_string = str(year)
    for index_1 in range(len(year_as_string)):
        for index_2 in range(len(year_as_string)):
            if index_1 == index_2:
                continue
            if year_as_string[index_1] == year_as_string[index_2]:
                happy_year = False
                break
        if not happy_year:
            break
    if happy_year:
        print(year)
        break
    else:
        year += 1
        happy_year = True