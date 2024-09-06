import unittest
import rt_with_exceptions as rt
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            cursor = rt.Runner(1, 10)
            for walk in range(10):
                cursor.walk()
            self.assertEqual(cursor.distance, 50)
            logging.info(f'"test_walk" выполнен успешно ')
        except:
            logging.info(f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            cursor = rt.Runner('Vasya', -5)
            for run in range(10):
                cursor.run()
            self.assertEqual(cursor.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    def test_challenge(self):
        cursor1 = rt.Runner('Petya')
        cursor2 = rt.Runner('Vanya')
        for move in range(10):
            cursor1.walk()
            cursor2.run()
        self.assertNotEqual(cursor1.distance, cursor2.distance)


logging.basicConfig(level=logging.INFO,
                    filemode="w",
                    filename='runner_tests.log',
                    encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s"
                    )
