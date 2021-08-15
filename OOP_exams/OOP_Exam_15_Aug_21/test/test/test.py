from project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Zoo")

    def test_init(self):
        self.assertEqual("Zoo", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food(self):
        res = self.shop.add_food("Food", 10)
        self.assertEqual("Successfully added 10.00 grams of Food.", res)
        self.assertEqual(self.shop.food["Food"], 10)
        self.shop.add_food("Food", 10)
        self.assertEqual(self.shop.food["Food"], 20)

    def test_add_food_invalid_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("Food", 0)
        self.assertEqual(str(ex.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_pet(self):
        res = self.shop.add_pet("Koko")
        self.assertEqual(res, "Successfully added Koko.")

    def test_add_pet_already_added(self):
        self.shop.add_pet("Koko")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Koko")
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_feed_pet(self):
        self.shop.food["Food"] = 1000
        self.shop.add_pet("Koko")
        res = self.shop.feed_pet("Food", "Koko")
        self.assertEqual(self.shop.food["Food"], 900)
        self.assertEqual(res, "Koko was successfully fed")

    def test_feed_pet_not_in_shop(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("Food", "Koko")
        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_with_invalid_food(self):
        self.shop.add_pet("Koko")
        res = self.shop.feed_pet("Food", "Koko")
        self.assertEqual(res, "You do not have Food")

    def test_feed_with_not_enough_food(self):
        self.shop.add_food("Food", 50)
        self.shop.add_pet("Koko")
        res = self.shop.feed_pet("Food", "Koko")
        self.assertEqual(self.shop.food["Food"], 1050)
        self.assertEqual(res, "Adding food...")

    def test_repr(self):
        self.shop.add_pet("Koko")
        self.shop.add_pet("Roko")
        self.shop.add_pet("Choco")
        res = self.shop.__repr__()
        self.assertEqual(res, 'Shop Zoo:\nPets: Koko, Roko, Choco')
