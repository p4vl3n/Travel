days = int(input())
doctors = 7
all_patients = 0
treated_patients = 0
untreated_patients = 0
all_treated_patients = 0
all_untreated_patients = 0
for day in range(1, days + 1):
    patients = int(input())
    all_patients += patients
    if doctors >= patients:
        treated_patients += patients
        all_treated_patients += treated_patients
    if day % 3 == 0:
        if all_treated_patients < all_untreated_patients:
            doctors += 1
    elif doctors < patients:
        treated_patients += doctors
        all_treated_patients += treated_patients
        untreated_patients = patients - doctors
        all_untreated_patients += untreated_patients
print(f'Treated patients: {all_treated_patients}.')
print(f'Untreated patients: {all_untreated_patients}.')
