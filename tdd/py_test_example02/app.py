import unittest 
from root_square_solver import rootSquareSolver

class CheckRootSquareSolver(unittest.TestCase):
    def test_check_two_roots(self):
        response = rootSquareSolver(1, -5, 6) # x² - 5x + 6 = 0 => r1 = 3 e r2 = 2
        self.assertEqual(len(response), 2)

    def test_check_root_value1(self):
        response = rootSquareSolver(1, -5, 6)
        # checa se o primeiro valor está contido no array
        self.assertIn(response[0], [2, 3])

    def test_check_root_value2(self):
        response = rootSquareSolver(1, -5, 6)
        # checa se o segundo valor está contido no array
        self.assertIn(response[1], [2, 3])  

    def test_check_one_roots(self):
        response = rootSquareSolver(1, -4, 4)
        
        self.assertEqual(len(response), 1)      
           