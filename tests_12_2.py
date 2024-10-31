from runer2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usein = Runner("Usein", 10)
        self.Andrey = Runner("Andrey", 9)
        self.Nic = Runner("Nic", 10)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            cls.all_results[i] = str(cls.all_results[i])
        print(cls.all_results)

    def test1(self):
        zabeg = Tournament(90, self.Usein, self.Nic)
        kak_mogno_dogadatsya = list(zabeg.participants)[-1]
        TournamentTest.all_results.update(zabeg.start())
        l = len(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[l], kak_mogno_dogadatsya)
        TournamentTest.tearDownClass()

    def test2(self):
        zabeg = Tournament(90, self.Andrey, self.Nic)
        kak_mogno_dogadatsya = list(zabeg.participants)[-1]
        TournamentTest.all_results.update(zabeg.start())
        l = len(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[l], kak_mogno_dogadatsya)
        TournamentTest.tearDownClass()

    def test3(self):
        zabeg = Tournament(90, self.Andrey, self.Usein, self.Nic)
        kak_mogno_dogadatsya = list(zabeg.participants)[-1]
        TournamentTest.all_results.update(zabeg.start())
        l = len(TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results[l], kak_mogno_dogadatsya)
        TournamentTest.tearDownClass()


if __name__ == "main":
    unittest.main()
