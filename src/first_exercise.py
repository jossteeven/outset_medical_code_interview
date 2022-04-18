class FirstExercise():

    def fizzbuzz(self,range_number):

        '''Given a n number this funtion will return the following outputs after analyse each number x from 0 to n:
            "FizzBuzz" if x is multiple of 3 and 5, 
            "Fizz" if x is only multiple of 3, 
            "Buzz" if x is only multiple of 5 and
            x for the other cases.   
            
            Args    range_number:   number of iterations

            Return  <"FizzBuzz">   if x is multiple of 3 and 5
                    <"Fizz">       if x is only multiple of 3
                    <"Buzz">       if x is only multiple of 5
                    <x>            x for the other cases
        '''
        iteration_outputs = []

        for number in range(range_number):
            prime_number = (number+1)
            if ( prime_number%3==0 and prime_number%5==0 ):
                iteration_outputs.append("FizzBuzz")
            elif ( prime_number%3==0 ):
                iteration_outputs.append("Fizz")
            elif (prime_number%5==0 ):
                iteration_outputs.append("Buzz")
            else:
                iteration_outputs.append(prime_number)
                
        return iteration_outputs
