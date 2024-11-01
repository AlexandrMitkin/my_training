from runer1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runer_walk = Runner("Vasya")
        for i in range(10):
            runer_walk.walk()
        '''
        прогулка
        '''
        self.assertEqual(runer_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runer_run = Runner("Dima")
        for i in range(10):
            runer_run.run()
        self.assertEqual(runer_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runer_walk2 = Runner("Goga")
        runer_run2 = Runner("Gosha")
        for i in range(10):
            runer_walk2.walk()
        for i in range(10):
            runer_run2.run()
        self.assertNotEqual(runer_walk2.distance, runer_run2.distance)


if __name__ == "main":
    unittest.main()
