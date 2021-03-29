country = input()
discipline = input()
difficulty = 0
execution = 0
if country == "Russia":
    if discipline == "ribbon":
        difficulty = 9.100
        execution = 9.400
    elif discipline == "hoop":
        difficulty = 9.300
        execution = 9.800
    elif discipline == "rope":
        execution = 9.000
        difficulty = 9.600
elif country == "Bulgaria":
    if discipline == "ribbon":
        difficulty = 9.600
        execution = 9.400
    elif discipline == "hoop":
        difficulty = 9.550
        execution = 9.750
    elif discipline == "rope":
        execution = 9.500
        difficulty = 9.400
elif country == "Italy":
    if discipline == "ribbon":
        difficulty = 9.200
        execution = 9.500
    elif discipline == "hoop":
        difficulty = 9.450
        execution = 9.350
    elif discipline == "rope":
        execution = 9.700
        difficulty = 9.150
score = execution + difficulty
percentage = (20 - score) / 20 * 100
print(f"The team of {country} get {score:.3f} on {discipline}.")
print(f"{percentage:.2f}%")