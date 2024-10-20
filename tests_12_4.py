import logging
from rt_with_exceptions import Runner as rn
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


def repeat(numb_repeat, *funcs):
    for func in funcs:
        for i in range(numb_repeat):
            func()


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            unit_1 = rn('Mr.Fox', -5)
            logging.info(f'"test_walk" выполнен успешно')
            repeat(10, unit_1.walk)
            self.assertEqual(unit_1.distance, 50)
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            unit_2 = rn(10)
            logging.info(f'"test_run" выполнен успешно')
            repeat(10, unit_2.run)
            self.assertEqual(unit_2.distance, 100)
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        unit_1 = rn('Mr.Fox')
        unit_2 = rn('lupus')
        repeat(10, unit_1.walk, unit_2.run)
        self.assertNotEqual(unit_1.distance, unit_2.distance)


if __name__ == '__main__':
    unittest.main()
