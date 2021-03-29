def take_odd(gvn_str):
    new_str = ""
    for i in range(len(gvn_str)):
        if i % 2:
            new_str += gvn_str[i]
    return new_str


def cut_str(gvn_str, i, l):
    new_str = gvn_str[:i] + gvn_str[i+l:]
    return new_str


def substitute(gvn_str, sbstr, sbst):
    new_str = gvn_str.replace(sbstr, sbst)
    return new_str


given_string = input()
command = input()
while not command == "Done":
    data = command.split()
    action = data[0]
    if action == "TakeOdd":
        given_string = take_odd(given_string)
        print(given_string)
    elif action == "Cut":
        index, length = int(data[1]), int(data[2])
        given_string = cut_str(given_string, index, length)
        print(given_string)
    elif action == "Substitute":
        substr, subst = data[1], data[2]
        if substr in given_string:
            given_string = substitute(given_string, substr, subst)
            print(given_string)
        else:
            print(f"Nothing to replace!")
    command = input()

print(f"Your password is: {given_string}")