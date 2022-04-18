class SecondExercise():

    def index_of_subarray(self,array_a, array_b):

        '''This function will search the first occurence of a small collection of elements (array_a) inside another collection of elements (array_b)
            
            Args    array_a:     collection of elements to search inside array_b
                    array_b:     collection of elements where array_a will be found

            Return  <integer>   index of first element of the small collection if found
                    <-1>        if the small collection is not found
        '''
        search_occurences = 0

        for b_element_index in range(len(array_b)) :
            for a_element_index in range(len(array_a)):
                iterable_position = b_element_index+a_element_index
                if iterable_position < len(array_b):
                    if array_a[a_element_index]==array_b[iterable_position]:
                        search_occurences+=1
                        if search_occurences == len (array_a):
                            return b_element_index
            search_occurences = 0
        return -1
        
            
# print(index_of_subarray(bigArray,smallArray))
# print(index_of_subarray(smallArray_t,bigArray_t))
# print(index_of_subarray(smallArray_s,bigArray_s))
# print(index_of_subarray.__doc__)