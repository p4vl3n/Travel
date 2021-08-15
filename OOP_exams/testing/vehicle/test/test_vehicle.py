import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(5.5, 100)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 5.5)
        self.assertEqual(self.vehicle.capacity, 5.5)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive(self):
        km = 2
        remaining_fuel = 3
        self.vehicle.drive(km)
        self.assertEqual(self.vehicle.fuel, remaining_fuel)

    def test_drive_exception(self):
        km = 5
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(km)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.drive(2)
        fuel = 2
        self.vehicle.refuel(fuel)
        self.assertEqual(self.vehicle.fuel, 5)

    def test_refuel_exception(self):
        fuel = 5
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        res = "The vehicle has 100 horse power with 5.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(res, str(self.vehicle))
