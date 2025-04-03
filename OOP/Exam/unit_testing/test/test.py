from project.star_system import StarSystem
from unittest import TestCase, main


class TestStarSystem(TestCase):
    def setUp(self):
        self.star_system = StarSystem("Test", 'Red giant', 'Single', 5, (0, 5))

    def test_init_with_habitable_zone_range(self):
        self.assertEqual("Test", self.star_system.name)
        self.assertEqual('Red giant', self.star_system.star_type)
        self.assertEqual('Single', self.star_system.system_type)
        self.assertEqual(5, self.star_system.num_planets)
        self.assertEqual((0, 5), self.star_system.habitable_zone_range)

    def test_init_without_habitable_zone_range(self):
        star_system = StarSystem("Test", 'Red giant', 'Single', 5)
        self.assertEqual("Test", star_system.name)
        self.assertEqual('Red giant', star_system.star_type)
        self.assertEqual('Single', star_system.system_type)
        self.assertEqual(5, star_system.num_planets)
        self.assertEqual(None, star_system.habitable_zone_range)

    def test_name_exception_raises(self):
        self.assertEqual("Test", self.star_system.name)
        with self.assertRaises(ValueError) as ex:
            self.star_system.name = "  "
        self.assertEqual("Name must be a non-empty string.", str(ex.exception))
        self.assertEqual("Test", self.star_system.name)

        self.assertEqual("Test", self.star_system.name)
        with self.assertRaises(ValueError) as ex:
            self.star_system.name = ""
        self.assertEqual("Name must be a non-empty string.", str(ex.exception))
        self.assertEqual("Test", self.star_system.name)

    def test_star_type_error_raises(self):
        self.star_system._STAR_TYPES = {'Red giant', 'Blue giant', 'Yellow dwarf', 'Red dwarf', 'Brown dwarf'}
        self.assertEqual('Red giant', self.star_system.star_type)
        with self.assertRaises(ValueError) as ex:
            self.star_system.star_type = "Test"
        self.assertEqual(f"Star type must be one of {sorted(self.star_system._STAR_TYPES)}.", str(ex.exception))
        self.assertEqual('Red giant', self.star_system.star_type)

    def test_system_type_error_raises(self):
        self.star_system._STAR_SYSTEM_TYPES = {'Single', 'Binary', 'Triple', 'Multiple'}
        self.assertEqual('Single', self.star_system.system_type)
        with self.assertRaises(ValueError) as ex:
            self.star_system.system_type = "Test"
        self.assertEqual(f"System type must be one of {sorted(self.star_system._STAR_SYSTEM_TYPES)}.",
                         str(ex.exception))
        self.assertEqual('Single', self.star_system.system_type)

    def test_num_planets_error_raises(self):
        self.assertEqual(5, self.star_system.num_planets)
        with self.assertRaises(ValueError) as ex:
            self.star_system.num_planets = -1
        self.assertEqual("Number of planets must be a non-negative integer.", str(ex.exception))
        self.assertEqual(5, self.star_system.num_planets)

    def test_habitable_zone_range_error_raises(self):
        self.assertEqual((0, 5), self.star_system.habitable_zone_range)
        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1,)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertEqual((0, 5), self.star_system.habitable_zone_range)

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1, 5, 10)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertEqual((0, 5), self.star_system.habitable_zone_range)

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (5, 3)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertEqual((0, 5), self.star_system.habitable_zone_range)

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (5, 5)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(ex.exception))
        self.assertEqual((0, 5), self.star_system.habitable_zone_range)

    def test__greater_than_error_raises(self):
        self.star_system.habitable_zone_range = None
        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10)
        with self.assertRaises(ValueError) as ex:
            self.star_system.__gt__(other_star_system)
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.",
                         str(ex.exception))
        self.star_system.habitable_zone_range = (5, 10)
        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10, )
        with self.assertRaises(ValueError) as ex:
            self.star_system.__gt__(other_star_system)
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.",
                         str(ex.exception))

    def test_greater_than_success(self):
        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10, (0, 3))
        self.assertEqual(other_star_system < self.star_system, self.star_system.__gt__(other_star_system))

        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10, (1, 6))
        self.assertEqual(other_star_system > self.star_system, self.star_system.__gt__(other_star_system))

        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10, (0, 5))
        self.assertEqual(other_star_system == self.star_system, self.star_system.__gt__(other_star_system))

    def test_compare_star_system_success(self):
        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10, (1, 6))
        method = self.star_system.compare_star_systems(self.star_system, other_star_system)
        self.assertEqual(
            f"{other_star_system.name} has a wider or equal habitable zone compared to {self.star_system.name}.",
            method)

        other_star_system = StarSystem("Testov", 'Blue giant', 'Binary', 10, (0, 3))
        method = self.star_system.compare_star_systems(self.star_system, other_star_system)
        self.assertEqual(f"{self.star_system.name} has a wider habitable zone than {other_star_system.name}.", method)

    def test_compare_star_system_error_raises(self):
        with self.assertRaises(NameError) as ex:
            self.star_system.compare_star_systems(self.star_system, other_star_system)
        self.assertEqual("name 'other_star_system' is not defined", str(ex.exception))


if __name__ == "__main__":
    main()
