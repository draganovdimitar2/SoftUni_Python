from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50.5, 150.5)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(150.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_error_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(44.25, self.vehicle.fuel)

    def test_refuel_error_raises(self):
        self.vehicle.fuel -= 15
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(16)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.fuel -= 15.5
        self.vehicle.refuel(5)
        self.assertEqual(40, self.vehicle.fuel)

    def test_str(self):
        result = f"The vehicle has {self.vehicle.horse_power} " \
                 f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(result, self.vehicle.__str__())


if __name__ == '__main__':
    main()
