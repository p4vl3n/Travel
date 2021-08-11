class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = [supply for supply in self.supplies if type(supply).__name__ == "FoodSupply"]
        if food_list:
            return food_list
        raise IndexError("There are no food supplies left!")
    
    @property
    def water(self):
        water_list = [supply for supply in self.supplies if type(supply).__name__ == "WaterSupply"]
        if water_list:
            return water_list
        raise IndexError("There are no water supplies left!")
    
    @property
    def painkillers(self):
        painkillers_list = [p for p in self.supplies if type(p).__name__ == "Painkiller"]
        if painkillers_list:
            return painkillers_list
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salves_list = [s for s in self.supplies if type(s).__name__ == "Salve"]
        if salves_list:
            return salves_list
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            medicine = [med for med in self.medicine if type(med).__name__ == medicine_type][-1]
            self.medicine.remove(medicine)
            medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            supply = [spl for spl in self.supplies if type(spl).__name__ == sustenance_type][-1]
            self.supplies.remove(supply)
            supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "Food")
            self.sustain(survivor, "Water")


