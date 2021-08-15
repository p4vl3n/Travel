import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Tommy", 10, 100, 50)

    def test_init(self):
        self.assertEqual("Tommy", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_lose(self):
        enemy_hero = Hero("Enemy", 1, 10000, 5)
        res = self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.health, 95)
        self.assertEqual(self.hero.damage, 50)
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(enemy_hero.health, 9505)
        self.assertEqual(enemy_hero.level, 2)
        self.assertEqual(enemy_hero.damage, 10)
        self.assertEqual("You lose", res)

    def test_battle_win(self):
        enemy_hero = Hero("Enemy", 1, 10, 5)
        res = self.hero.battle(enemy_hero)
        self.assertEqual("You win", res)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 55)
        self.assertEqual(self.hero.level, 11)


    def test_battle_draw(self):
        enemy_hero = Hero("Enemy", 10, 100, 50)
        res = self.hero.battle(enemy_hero)
        self.assertEqual("Draw", res)

    def test_battle_self(self):
        enemy_hero = Hero("Tommy", 10, 100, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_no_health(self):
        self.hero.health -= 100
        enemy_hero = Hero("Enemy", 10, 100, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_no_health(self):
        enemy_hero = Hero("Enemy", 10, 0, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))

    def test_str(self):
        res = str(self.hero)
        test_message = "Hero Tommy: 10 lvl\nHealth: 100\nDamage: 50\n"
        self.assertEqual(res, test_message)