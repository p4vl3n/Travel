from sys import maxsize
biggest_num = -maxsize
for num in range(3):
    given_num = int(input())
    if given_num > biggest_num:
        biggest_num = given_num
print(biggest_num)