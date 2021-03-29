friends = int(input())
nights = int(input())
bus_tickets = int(input())
museum_tickets = int(input())
price_per_night = 20
bus_ticket_cost = 1.60
museum_ticket_cost = 6
transport_cost = bus_tickets * bus_ticket_cost
museum_cost = museum_tickets * museum_ticket_cost
stay_cost = nights * price_per_night
cost_for_friend = transport_cost + museum_cost + stay_cost
total_cost = cost_for_friend * friends * 1.25
print(f'{total_cost:.2f}')