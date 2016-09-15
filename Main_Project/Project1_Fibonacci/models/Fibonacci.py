from django.db import models
import time

# Create your models here.
class Fibonacci:
    
    # recusive programming approach
    @classmethod
    def recursive_fib(self,input_number):
        if input_number >=0 :
            if input_number <=1:
                return input_number
            else:
                return Fibonacci.recursive_fib(input_number-1) + Fibonacci.recursive_fib(input_number-2)
        

    # using dynamic programming concept, avoid recalculation of already computed number 
    # by storing the result
    @classmethod
    def fib(self,input_number):
        
        if input_number <=1:
            return input_number

        else:
            dp = [None]*(input_number+1)
            dp[0] = 0
            dp[1] = 1
            for i in range(2,input_number+1):
                dp[i] = dp[i-1]+dp[i-2]

            return dp[input_number]

    
    