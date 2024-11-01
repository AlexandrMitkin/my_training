from runer4 import Runner
# import unittest
import logging


# logger = logging.getLogger(__name__)


# class RunnerTest(unittest.TestCase):
class RunnerTest:
    is_frozen = False

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runer_walk = Runner("Vasya")
            for i in range(10):
                runer_walk.walk()
            # self.assertEqual(runer_walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            return
        '''
        прогулка
        '''

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runer_run = Runner(5)
            for i in range(10):
                runer_run.run()
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return

        # self.assertEqual(runer_run.distance, 100)

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runer_walk2 = Runner("Goga")
        runer_run2 = Runner("Gosha")
        for i in range(10):
            runer_walk2.walk()
        for i in range(10):
            runer_run2.run()
        # self.assertNotEqual(runer_walk2.distance, runer_run2.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", encoding='utf-8', filename="runner_tests.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    # unittest.main()
    RunnerTest().test_walk()
    RunnerTest().test_run()
