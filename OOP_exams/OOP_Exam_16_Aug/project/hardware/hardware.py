class Hardware:
    def __init__(self, name, type_, capacity, memory):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if not software.capacity_consumption <= self.capacity or not software.memory_consumption <= self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

