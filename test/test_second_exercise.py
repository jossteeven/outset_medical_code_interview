import unittest

from src.second_exercise import SecondExercise

class TestSecondExercise(unittest.TestCase):
    
    # List
    collection_a_l = ["a","b","c"]
    collection_b_l = ["a","c","a","b","c","x","a","b"]
    
    # Tuple
    collection_a_t = ("a","b","c")
    collection_b_t = ("a","c","a","b","c","x","a","b")

    # String 
    collection_a_s = "abc"
    collection_b_s = "acabcxab"

    def test_index_of_subarray_return_integer_when_found_in_list(self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_a_l,self.collection_b_l)
        self.assertGreaterEqual(result,0)

    def test_index_of_subarray_return_integer_when_found_in_tuple(self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_a_t,self.collection_b_t)
        self.assertGreaterEqual(result,0)
    
    def test_index_of_subarray_return_integer_when_found_in_string(self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_a_s,self.collection_b_s)
        self.assertGreaterEqual(result,0)

    # Tests when search not found

    def test_index_of_subarray_return_integer_when_not_found_in_list(self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_b_l,self.collection_a_l)
        self.assertEqual(result,-1)

    def test_index_of_subarray_return_integer_when_not_found_in_tuple(self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_b_t,self.collection_a_t)
        self.assertEqual(result,-1)
    
    def test_index_of_subarray_return_integer_when_not_found_in_string(self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_b_s,self.collection_a_s)
        self.assertEqual(result,-1)


    def test_index_of_subarray_return_integer_when_found_in_equal_lists (self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_a_s,self.collection_a_s)
        self.assertGreaterEqual(result,0)
    def test_index_of_subarray_return_integer_when_found_in_equal_tuples (self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_b_t,self.collection_b_t)
        self.assertGreaterEqual(result,0)

    def test_index_of_subarray_return_integer_when_found_in_equal_strings (self):

        search_instance = SecondExercise()
        result = search_instance.index_of_subarray(self.collection_a_s,self.collection_a_s)
        self.assertGreaterEqual(result,0)

if __name__ == '__main__':
    unittest.main()