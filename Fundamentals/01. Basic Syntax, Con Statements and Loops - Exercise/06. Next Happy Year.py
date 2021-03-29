this_year = int(input())
ongoing_check = True
while ongoing_check:
    this_year += 1
    checking_year = str(this_year)
    if len(set(checking_year)) == len(checking_year):
        ongoing_check = False
        print(this_year)
        break
