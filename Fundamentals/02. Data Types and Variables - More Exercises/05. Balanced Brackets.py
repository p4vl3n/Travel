lines = int(input())
inspected_string = ""
for line in range(lines):
    given_input = input()
    inspected_string += given_input
left_bracket = inspected_string.count("(")
right_bracket = inspected_string.count(")")
if left_bracket == right_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")
