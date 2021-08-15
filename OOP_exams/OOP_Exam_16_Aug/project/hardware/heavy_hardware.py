from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", 2 * capacity, 0.75 * memory)

