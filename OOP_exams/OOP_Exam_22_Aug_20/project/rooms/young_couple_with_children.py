from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        family_count = 2 + len(children)
        super().__init__(family_name, (salary_one + salary_two), family_count)
        self.room_cost = 30
        self.children = [child for child in children]
        self.appliances = [TV(), Fridge(), Laptop()] * family_count
        self.calculate_expenses(self.appliances, self.children)
