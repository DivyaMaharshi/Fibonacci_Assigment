from django.db import models


# Create your models here.
class Fibonacci:

    @classmethod
    def fib(self, input_number):
        
        if input_number <=1:
            return input_number

        else:
            dp = [None]*(input_number+1)
            dp[0] = 0
            dp[1] = 1
            
            for i in range(2,input_number+1):
                dp[i] = dp[i-1]+dp[i-2]

            return dp[input_number]

    
    