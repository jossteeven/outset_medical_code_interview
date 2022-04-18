import unittest

from src.first_exercise import FirstExercise

class TestFirstExercise(unittest.TestCase):
    
    # Cases Condition n>=0
    n_1 = 0
    n_2 = 15

    def test_fizzbuzz_when_range_number_equal_0(self):

        search_instance = FirstExercise()
        result = search_instance.fizzbuzz(self.n_1)
        self.assertEqual(result,[])
    
    def test_fizzbuzz_when_range_number_greater_than_0(self):

        search_instance = FirstExercise()
        result = search_instance.fizzbuzz(self.n_1)
        for index in range(self.n_1):
            prime_number = index+1
            if prime_number%3==0 and prime_number%5==0:
                self.assertEqual(result[number],"FizzBuzz")
            elif prime_number%3==0:
                self.assertEqual(result[number],"Fizz")
            elif prime_number%3==0:
                self.assertEqual(result[number],"Buzz")
            else:
                self.assertEqual(result[number],prime_number)
        

if __name__ == '__main__':
    unittest.main()