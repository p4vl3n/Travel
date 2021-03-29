movie = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
while movie != "Finish":
    hall_capacity = int(input())
    tickets_sold = 0
    while tickets_sold < hall_capacity:
        ticket_type = input()
        if ticket_type == "End":
            break
        tickets_sold += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
    print(f'{movie} - {tickets_sold / hall_capacity * 100:.2f}% full.')
    movie = input()
total_tickets = student_tickets + standard_tickets + kids_tickets
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kids_tickets / total_tickets * 100:.2f}% kids tickets.')