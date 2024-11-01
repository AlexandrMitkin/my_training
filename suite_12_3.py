import unittest
import tests_12_1_3
import tests_12_2_3

testsuit_run = unittest.TestSuite()
# testsuit_run.addTest(unittest.makeSuite(tests_12_1.RunnerTest))
# testsuit_run.addTest(unittest.makeSuite(tests_12_2.TournamentTest))
testsuit_run.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1_3.RunnerTest))
testsuit_run.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2_3.TournamentTest))
run_testsuit_run = unittest.TextTestRunner(verbosity=2)

run_testsuit_run.run(testsuit_run)
