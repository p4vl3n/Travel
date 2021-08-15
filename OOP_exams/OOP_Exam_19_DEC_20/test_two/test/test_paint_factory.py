from project.factory.paint_factory import PaintFactory
import unittest


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Test", 100)

    def test_init(self):
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        colors = ["white", "yellow", "blue", "green", "red"]
        self.assertEqual(colors, self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)

    def test_add_ingredient_successful(self):
        ingredient = "white"
        self.factory.add_ingredient(ingredient, 10)
        self.assertEqual(self.factory.ingredients, {"white": 10})
        self.factory.add_ingredient(ingredient, 10)
        self.assertEqual(self.factory.ingredients, {"white": 20})

    def test_add_ingredient_unsuccessful_no_space(self):
        ingredient = "white"
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient(ingredient, 101)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_ingredient_unsupported_type(self):
        ingredient = "amber"
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient(ingredient, 101)
        self.assertEqual(str(ex.exception), f"Ingredient of type {ingredient} not allowed in PaintFactory")

    def test_remove_ingredient_successful(self):
        ingredient = "white"
        self.factory.add_ingredient(ingredient, 50)
        self.factory.remove_ingredient(ingredient, 49)
        self.assertEqual(self.factory.ingredients[ingredient], 1)

    def test_remove_ingredient_unsuccessful(self):
        ingredient = "white"
        self.factory.add_ingredient(ingredient, 50)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient(ingredient, 51)
        self.assertEqual(str(ex.exception), "Ingredients quantity cannot be less than zero")

    def test_remove_ingredient_not_found(self):
        ingredient = "white"
        self.factory.add_ingredient(ingredient, 50)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("amber", 51)
        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")

