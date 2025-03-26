from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.test_hero = Hero("Test", 5, 99.9, 25.5)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.test_hero.username, str)
        self.assertIsInstance(self.test_hero.health, float)
        self.assertIsInstance(self.test_hero.damage, float)
        self.assertIsInstance(self.test_hero.level, int)

    def test_init(self):
        self.assertEqual("Test", self.test_hero.username)
        self.assertEqual(5, self.test_hero.level)
        self.assertEqual(99.9, self.test_hero.health)
        self.assertEqual(25.5, self.test_hero.damage)

    def test_battle_enemy_hero_name_the_same_error_raises(self):
        opponent = Hero("Test", 5, 99.5, 22.2)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(opponent)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_below_or_equal_zero_error_raises(self):
        opponent = Hero("Test1", 5, 99.5, 22.2)
        self.test_hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(opponent)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.test_hero.health = -1
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(opponent)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_below_or_equal_zero_error_raises(self):
        opponent = Hero("Test1", 5, 0, 22.2)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(opponent)

        self.assertEqual(f"You cannot fight {opponent.username}. He needs to rest", str(ex.exception))

        opponent = Hero("Test1", 5, -1, 22.2)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(opponent)

        self.assertEqual(f"You cannot fight {opponent.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        self.test_hero.health = 100.0
        self.test_hero.damage = 20
        opponent = Hero("Test1", 5, 100.0, 20)

        result = self.test_hero.battle(opponent)
        self.assertEqual(0, self.test_hero.health)
        self.assertEqual(5, self.test_hero.level)
        self.assertEqual(20, self.test_hero.damage)

        self.assertEqual(0, opponent.health)
        self.assertEqual(5, opponent.level)
        self.assertEqual(20, opponent.damage)

        self.assertEqual("Draw", result)

    def test_battle_hero_wins(self):
        self.test_hero.health = 200
        opponent = Hero("Test1", 5, 1, 20)
        result = self.test_hero.battle(opponent)
        self.assertEqual(6, self.test_hero.level)
        self.assertEqual(105, self.test_hero.health)
        self.assertEqual(30.5, self.test_hero.damage)
        self.assertEqual("You win", result)

        self.assertEqual(5, opponent.level)
        self.assertEqual(-126.5, opponent.health)
        self.assertEqual(20, opponent.damage)

    def test_battle_hero_loses(self):
        self.test_hero.health = 120
        opponent = Hero("Test1", 5, 200, 20)
        result = self.test_hero.battle(opponent)
        self.assertEqual(5, self.test_hero.level)
        self.assertEqual(20, self.test_hero.health)
        self.assertEqual(25.5, self.test_hero.damage)
        self.assertEqual("You lose", result)

        self.assertEqual(6, opponent.level)
        self.assertEqual(77.5, opponent.health)
        self.assertEqual(25, opponent.damage)

    def test_str(self):
        result = f"Hero {self.test_hero.username}: {self.test_hero.level} lvl\n" \
                 f"Health: {self.test_hero.health}\n" \
                 f"Damage: {self.test_hero.damage}\n"
        self.assertEqual(result, self.test_hero.__str__())


if __name__ == "__main__":
    main()
