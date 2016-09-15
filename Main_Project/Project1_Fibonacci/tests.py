from django.test import TestCase
from Project1_Fibonacci import Fibonacci 

#test cases
#command : python manage.py test Project1_Fibonacci.tests

assert(Fibonacci.mulplicative_fib(0) ==  0)
assert(Fibonacci.mulplicative_fib(1) == 1)
assert(Fibonacci.mulplicative_fib(2) == 1)
assert(Fibonacci.mulplicative_fib(9) == 34)
assert(Fibonacci.mulplicative_fib(10) == 55)
assert(Fibonacci.mulplicative_fib(50) == 12586269025)
assert(Fibonacci.mulplicative_fib(100) == 354224848179261915075)




