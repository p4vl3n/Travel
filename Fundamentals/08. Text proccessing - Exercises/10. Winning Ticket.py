def ticket_is_valid(tkt):
    if len(tkt) == 20:
        return True
    return False

given_tickets = input().split(", ")
tickets = []
valid_chars = ['@', '#', '$', '^']
for ticket in given_tickets:
    tickets.append(ticket.strip())
for ticket in tickets:
    if ticket_is_valid(ticket):
        left_side = ticket[0:10]
        right_side = ticket[10:len(ticket)]
        occurances = 0
        continiuous = False
        for i in range(len(left_side)-1):
            if left_side[i] in valid_chars:
                if left_side[i] == left_side[i+1]:
                    continiuous = True
                else:
                    continiuous = False
                if continiuous:
                    occurances += 1
            
    else:
        print(f"invalid ticket")