def loading_bar(x):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",]
    percentage = int(x/10)
    for percent in range(percentage):
        bar[percent] = "%"
    if x == 100:
        return f"100% Complete!\n[{''.join(bar)}]"
    return f"{x}% [{''.join(bar)}]\nStill loading..."


given_num = int(input())
result = loading_bar(given_num)
print(result)