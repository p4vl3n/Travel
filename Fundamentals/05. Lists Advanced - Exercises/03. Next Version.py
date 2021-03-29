# current_version = [int(x) for x in input().split(".")]
current_version = input().split(".")
formatted_old_version = "".join(current_version)
updated_version = str(int(formatted_old_version) + 1)
print(".".join(updated_version))

