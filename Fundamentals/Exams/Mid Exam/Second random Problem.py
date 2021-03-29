# You will be given a series of strings on a single line, separated by one whitespace.
# These represent the collection you will be working with.
# On the next input lines until you receive the command "end", you'll receive a series
# of commands in one of the following formats:
# - reverse from [start] count [count] -- this instructs you to reverse a portion of the array -
# just [count] elements starting at index [start];
# - sort from [start] count [count] - this instructs you to sort a portion of the array - [count]
# elements starting at index [start];
# - remove [count] - remove the first count elements

# Note: commands will always be valid and in the range of the array
# After you're done, print the resulting elements joined by ", ".
# The examples should help you understand the task better.

# Input
# - The input data should be read from the console
# - The first input line will hold a series of strings, separated by one whitespace
# - The next lines will hold commands in the described formats (exactly)
# - The input ends with the keyword "end"
# - The input data will always be valid and in the format described.
# There is no need to check it explicitly

# Output
# - The output should be printed on the console
# - After receiving the "end" command, print the resulting array on the console
# in the format specified above.

# Constraints
# - The count of strings in the collection will be in the range [1...50]
# - The number of commands will be in the range [1..20]
# - All commands will be in the described format
# - [start] and [count] will be integers in the range [-sysmax ... +sysmax]
given_string = input().split()
command = input()
while not command == "end":

    command = input()