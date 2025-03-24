class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class TestWorker(TestCase):
    def test_worker_init(self):
        worker = Worker("Ivan", 2500, 100)  # Arrange and act
        # Assert
        self.assertEqual("Ivan", worker.name)
        self.assertEqual(2500, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_has_no_energy_work_raises(self):
        # Test with 0 energy
        # Arrange
        worker = Worker("Ivan", 2500, 0)

        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()

        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(worker.money, 0)
        self.assertEqual(worker.energy, 0)

        # Test with negative energy
        worker.energy = -1
        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()

        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(worker.money, 0)
        self.assertEqual(worker.energy, -1)

    def test_worker_works(self):
        # Test with positive energy
        # Arrange
        worker = Worker("Ivan", 2500, 2)
        self.assertEqual(0, worker.money)
        self.assertEqual(2, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(2500, worker.money)
        self.assertEqual(1, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(5000, worker.money)
        self.assertEqual(0, worker.energy)

    def test_worker_rest_increase_energy(self):
        worker = Worker("Ivan", 2500, 0)
        self.assertEqual(0, worker.energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(1, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Ivan", 2500, 0)
        # Act & Assert
        self.assertEqual(f'Ivan has saved 0 money.', worker.get_info())


if __name__ == "__main__":
    main()
