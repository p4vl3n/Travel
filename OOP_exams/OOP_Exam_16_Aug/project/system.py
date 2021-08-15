from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(software)
        except Exception as e:
            return str(e)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware[0].install(software)
        except Exception as e:
            return str(e)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        software = [soft for soft in System._software if soft.name == software_name]
        if not (hardware and software):
            return "Some of the components do not exist"
        hardware_component = hardware[0]
        software_component = software[0]
        hardware_component.uninstall(software_component)
        System._software.remove(software_component)

    @staticmethod
    def analyze():
        total_capacity = sum([hard.capacity for hard in System._hardware])
        total_memory = sum([hard.memory for hard in System._hardware])
        capacity_consumed = sum([soft.capacity_consumption for soft in System._software])
        memory_consumed = sum([soft.memory_consumption for soft in System._software])
        message = "System Analysis\n"
        message += f"Hardware Components: {len(System._hardware)}\n"
        message += f"Software Components: {len(System._software)}\n"
        message += f"Total Operational Memory: {memory_consumed:.0f} / {total_memory:.0f}\n"
        message += f"Total Capacity Taken: {capacity_consumed:.0f} / {total_capacity:.0f}"
        return message

    @staticmethod
    def system_split():
        sys_split_info = []
        for hardware in System._hardware:
            message = f"Hardware Component - {hardware.name}\n"
            message += f"Express Software Components: " \
                       f"{len([soft for soft in hardware.software_components if soft.type == 'Express'])}\n"
            message += f"Light Software Components: " \
                       f"{len([soft for soft in hardware.software_components if soft.type == 'Light'])}\n"
            message += f"Memory Usage: " \
                       f"{sum([soft.memory_consumption for soft in hardware.software_components]):.0f} " \
                       f"/ {hardware.memory:.0f}\n"
            message += f"Capacity Usage: " \
                       f"{sum([soft.capacity_consumption for soft in hardware.software_components]):.0f} " \
                       f"/ {hardware.capacity:.0f}\n"
            message += f"Type: {hardware.type}\n"
            message += "Software Components: "
            if hardware.software_components:
                components = ', '.join([soft.name for soft in hardware.software_components])
                message += components
            else:
                message += "None"
            sys_split_info.append(message)
        final_msg = '\n'.join(sys_split_info)
        return final_msg

