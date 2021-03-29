import re


text = input()
pattern = r"\b_{1}[a-zA-Z0-9]+\b"
valid_variables = re.findall(pattern, text)
vars_to_print = []
for variable in valid_variables:
    variable = variable[1:len(variable)]
    vars_to_print.append(variable)
print(",".join(vars_to_print))