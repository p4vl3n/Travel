from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", 0.25 * capacity, 1.75 * memory)

