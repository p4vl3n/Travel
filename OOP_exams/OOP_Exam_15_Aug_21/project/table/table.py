from abc import ABC, abstractmethod


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value
    
    @property
    def is_reserved(self):
        return self.__is_reserved

    @is_reserved.setter
    def is_reserved(self, value):
        self.__is_reserved = value

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        table_bill = 0
        table_bill += sum(drink.price for drink in self.drink_orders)
        table_bill += sum(food.price for food in self.food_orders)
        return table_bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            message = f"Table: {self.table_number}\n"
            message += f"Type: {self.__class__.__name__}\n"
            message += f"Capacity: {self.capacity}"
            return message
