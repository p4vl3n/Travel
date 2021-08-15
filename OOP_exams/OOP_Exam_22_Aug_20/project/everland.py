class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        messages = []
        for room in self.rooms:
            total_expense = room.expenses + room.room_cost
            if room.budget >= total_expense:
                room.budget -= total_expense
                messages.append(f"{room.family_name} paid {total_expense:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                messages.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(messages)

    def status(self):
        message = f"Total population: {sum([room.members_count for room in self.rooms])}\n"

        for room in self.rooms:
            message += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, " \
                       f"Expenses: {room.expenses:.2f}$\n"
            if room.children:
                counter = 0
                for child in room.children:
                    counter += 1
                    message += f"--- Child {counter} monthly cost {child.cost * 30:.2f}$\n"
            if hasattr(room, 'appliances'):
                total_expenses = 0
                for a in room.appliances:
                    total_expenses += a.get_monthly_expense()
                message += f"--- Appliances monthly cost: {total_expenses:.2f}$\n"

        return message

