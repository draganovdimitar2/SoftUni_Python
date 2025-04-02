from project.furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):
    def setUp(self):
        self.furniture = Furniture('Test', 50, (5, 5, 5), False, 50.5)

    def test_init_furniture_not_in_stock_and_weight(self):
        self.assertEqual('Test', self.furniture.model)
        self.assertEqual(50, self.furniture.price)
        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        self.assertEqual(False, self.furniture.in_stock)
        self.assertEqual(50.5, self.furniture.weight)

    def test_init_furniture_in_stock_without_weight(self):
        furniture = Furniture('Testov', 120, (10, 10, 10))
        self.assertEqual('Testov', furniture.model)
        self.assertEqual(120, furniture.price)
        self.assertEqual((10, 10, 10), furniture.dimensions)
        self.assertEqual(True, furniture.in_stock)
        self.assertEqual(None, furniture.weight)

    def test_model_error_raises(self):
        self.assertEqual('Test', self.furniture.model)
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = ''
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))
        self.assertEqual('Test', self.furniture.model)

        self.assertEqual('Test', self.furniture.model)
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = '   '
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))
        self.assertEqual('Test', self.furniture.model)

        with self.assertRaises(ValueError) as ex:
            self.furniture.model = 55 * "a"  # test with 50+ chars
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))
        self.assertEqual('Test', self.furniture.model)

    def test_model_success(self):
        self.assertEqual('Test', self.furniture.model)
        self.furniture.model = 'Testov'
        self.assertEqual('Testov', self.furniture.model)

    def test_price_error(self):
        self.assertEqual(50, self.furniture.price)
        with self.assertRaises(ValueError) as ex:
            self.furniture.price = -1  # test with negative int
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))
        self.assertEqual(50, self.furniture.price)

    def test_price_success(self):
        self.assertEqual(50, self.furniture.price)
        self.furniture.price = 150
        self.assertEqual(150, self.furniture.price)

    def test_dimensions_error_raises(self):
        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (5, 5)  # test with tuple with 2 elements
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))
        self.assertEqual((5, 5, 5), self.furniture.dimensions)

        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (5, 5, 5, 5)  # test with tuple with 4 elements
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))
        self.assertEqual((5, 5, 5), self.furniture.dimensions)

        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (0, 5, 5)  # test with element equal to 0
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))
        self.assertEqual((5, 5, 5), self.furniture.dimensions)

        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (5, -1, 5)  # test with negative element
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))
        self.assertEqual((5, 5, 5), self.furniture.dimensions)

        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (0, 0, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))
        self.assertEqual((5, 5, 5), self.furniture.dimensions)

    def test_dimensions_success(self):
        self.assertEqual((5, 5, 5), self.furniture.dimensions)
        self.furniture.dimensions = (6, 6, 6)
        self.assertEqual((6, 6, 6), self.furniture.dimensions)

    def test_weight_error_raises(self):
        self.assertEqual(50.5, self.furniture.weight)
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = -2.2  # test with negative int
        self.assertEqual(50.5, self.furniture.weight)

    def test_available_status(self):
        result = 'Model: Test is currently unavailable.'  # test with in_stock == False
        self.assertEqual(result, self.furniture.get_available_status())

        self.furniture.in_stock = True
        result = (f"Model: Test is currently "
                  'in stock.')
        self.assertEqual(result, self.furniture.get_available_status())

    def test_get_specifications(self):
        result = (f"Model: Test has the following dimensions: "
                  f"5mm x 5mm x 5mm and weighs: 50.5")
        self.assertEqual(result, self.furniture.get_specifications())

        self.furniture.weight = None
        result = (f"Model: Test has the following dimensions: "
                  f"5mm x 5mm x 5mm and weighs: N/A")
        self.assertEqual(result, self.furniture.get_specifications())


if __name__ == '__main__':
    main()
