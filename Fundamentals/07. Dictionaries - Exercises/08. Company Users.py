companies = {}
command = input()
while not command == "End":
    company, identity = command.split(" -> ")
    if company not in companies:
        companies[company] = []
    if identity not in companies[company]:
        companies[company].append(identity)
    command = input()
sorted_companies = dict(sorted(companies.items(), key=lambda x: x[0]))
for company, identities in sorted_companies.items():
    print(f"{company}")
    for identity in identities:
        print(f"-- {identity}")