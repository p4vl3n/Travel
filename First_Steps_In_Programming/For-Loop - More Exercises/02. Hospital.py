days = int(input())
doctors = 7
all_patients = 0
treated = 0
for period in range(1, days + 1):
    patients = int(input())
    if period % 3 == 0 and (treated != 0 and (all_patients / treated) )> 2:
        doctors += 1
    if doctors >= patients:
        treated += patients
    else:
        treated += doctors
    all_patients += patients
print(f'Treated patients: {treated}.')
print(f'Untreated patients: {all_patients - treated}.')