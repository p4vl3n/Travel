file_path = input().split("\\")
working_string = file_path[-1].split(".")
print(f"File name: {working_string[0]}")
print(f"File extension: {working_string[1]}")
