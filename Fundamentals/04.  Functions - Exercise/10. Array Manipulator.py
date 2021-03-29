from sys import maxsize


def exchange(lst, index):
    new_list = lst[index+1:] + lst[:index+1]
    return new_list


def max_odd_even(lst, action):
    biggest = -maxsize
    index = ""
    if action == "odd":
        it_matches = True
        for num in range(len(lst)):
            if not lst[num] % 2 == 0 and lst[num] >= biggest:
                biggest = lst[num]
                index = num
        if biggest == -maxsize:
            it_matches = False
        if it_matches:
            return index
        else:
            return "No matches"
    elif action == "even":
        it_matches = True
        for num in range(len(lst)):
            if lst[num] % 2 == 0 and lst[num] >= biggest:
                biggest = lst[num]
                index = num
        if biggest == -maxsize:
            it_matches = False
        if it_matches:
            return index
        else:
            return "No matches"


def min_odd_even(lst, action):
    smallest = maxsize
    index = ""
    if action == "odd":
        it_matches = True
        for num in range(len(lst)):
            if not lst[num] % 2 == 0 and lst[num] <= smallest:
                smallest = lst[num]
                index = num
        if smallest == maxsize:
            it_matches = False
        if it_matches:
            return index
        else:
            return "No matches"
    elif action == "even":
        it_matches = True
        for num in range(len(lst)):
            if lst[num] % 2 == 0 and lst[num] <= smallest:
                smallest = lst[num]
                index = num
        if smallest == maxsize:
            it_matches = False
        if it_matches:
            return index
        else:
            return "No matches"


def first_odd_even(lst, index, odd_or_even):
    if odd_or_even == "odd":
        first_n_odd = []
        for n in range(len(lst)):
            if not lst[n] % 2 == 0:
                first_n_odd.append(lst[n])
        first_n_odd = first_n_odd[:index:]
        return first_n_odd
    elif odd_or_even == "even":
        first_n_even = []
        for n in range(len(lst)):
            if lst[n] % 2 == 0:
                first_n_even.append(lst[n])
        first_n_even = first_n_even[:index:]
        return first_n_even


def last_odd_even(lst, index, odd_or_even):
    if odd_or_even == "odd":
        last_n_odd = []
        for n in range(len(lst)):
            if not lst[n] % 2 == 0:
                last_n_odd.append(lst[n])
        last_n_odd = last_n_odd[-1:-index-1:-1]
        last_n_odd.reverse()
        return last_n_odd
    elif odd_or_even == "even":
        last_n_even = []
        for n in range(len(lst)):
            if lst[n] % 2 == 0:
                last_n_even.append(lst[n])
        last_n_even = last_n_even[-1:-index-1:-1]
        last_n_even.reverse()
        return last_n_even


array = [int(x) for x in input().split()]
command = input()

while not command == "end":
    command_list = command.split()

    if command_list[0] == "exchange":
        if len(array) > int(command_list[1]) >= 0:
            array = exchange(array, int(command_list[1]))
        else:
            print("Invalid index")

    elif command_list[0] == "max":
        print(max_odd_even(array, command_list[1]))

    elif command_list[0] == "min":
        print(min_odd_even(array, command_list[1]))

    elif command_list[0] == "first":
        if int(command_list[1]) > len(array):
            print("Invalid count")
        else:
            print(first_odd_even(array, int(command_list[1]), command_list[2]))

    elif command_list[0] == "last":
        if int(command_list[1]) > len(array):
            print("Invalid count")
        else:
            print(last_odd_even(array, int(command_list[1]), command_list[2]))
    command = input()

print(array)
