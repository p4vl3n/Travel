from project.table.table import Table
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.baked_food.baked_food import BakedFood
from project.baked_food.cake import Cake
from project.baked_food.bread import Bread

from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        if not tables:
            return f"Could not find table {table_number}"
        table = tables[0]
        not_on_the_menu = []
        for food_order in args:
            if food_order not in [f.name for f in self.food_menu]:
                not_on_the_menu.append(food_order)
            else:
                food = [f for f in self.food_menu if f.name == food_order][0]
                table.order_food(food)
            # food_order_available = False
            # for food_option in self.food_menu:
            #     if food_order == food_option.name:
            #         table.order_food(food_option)
            #         food_order_available = True
            # if not food_order_available:
            #     not_on_the_menu.append(food_order)

        message = f"Table {table_number} ordered:\n"
        message += '\n'.join(str(food) for food in table.food_orders)
        message += f"\n{self.name} does not have in the menu:\n"
        message += '\n'.join(not_on_the_menu)
        return message

    def order_drink(self, table_number, *args):
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        if not tables:
            return f"Could not find table {table_number}"
        table = tables[0]
        not_on_the_menu = []
        for drink_order in args:
            if drink_order not in [d.name for d in self.drinks_menu]:
                not_on_the_menu.append(drink_order)
            else:
                drink = [d for d in self.drinks_menu if d.name == drink_order][0]
                table.order_drink(drink)
        # for drink_order in args:
        #     drink_order_available = False
        #     for drink_option in self.drinks_menu:
        #         if drink_order == drink_option.name:
        #             table.order_drink(drink_option)
        #             drink_order_available = True
        #     if not drink_order_available:
        #         not_on_the_menu.append(drink_order)

        message = f"Table {table_number} ordered:\n"
        message += '\n'.join(str(drink) for drink in table.drink_orders)
        message += f"\n{self.name} does not have in the menu:\n"
        message += '\n'.join(not_on_the_menu)
        return message

    def leave_table(self, table_number):
        possible_table = [table for table in self.tables_repository if table.table_number == table_number]
        table = possible_table[0]
        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        message = f"Table: {table_number}\nBill: {bill:.2f}"
        return message

    def get_free_tables_info(self):
        message = []
        for table in self.tables_repository:
            if not table.is_reserved:
                message.append(table.free_table_info())
        return '\n'.join(message)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


shop = Bakery("Koko")
print(shop.add_table("InsideTable", 1, 3))
print(shop.get_free_tables_info())
print(shop.get_total_income())