def data_type(action, el):
    result = ""
    if action == "int":
        result = int(el) * 2
    elif action == "real":
        result = f"{float(el) * 1.5:.2f}"
    elif action == "string":
        result = f"${el}$"
    return result


given_action = input()
element = input()
print(data_type(given_action, element))
