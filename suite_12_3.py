import unittest
import tests_12_2
import tests_12_1

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(runST)
