usernames = input().split(", ")
valids = []
for username in usernames:
    if 3 <= len(username) <= 16:
        if "-" in username:
            check_user = username.replace("-", "0")
            if check_user.isalnum():
                valids.append(username)
        elif "_" in username:
            check_user = username.replace("_", "0")
            if check_user.isalnum():
                valids.append(username)
        elif username.isalnum():
            valids.append(username)
print("\n".join(valids))