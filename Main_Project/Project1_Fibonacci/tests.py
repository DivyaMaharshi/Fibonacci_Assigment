from django.test import TestCase

# Create your tests here.
from Project1_Fibonacci.views import fib

assert(fib(0) ==  0)
assert(fib(1) == 1)
assert(fib(2) == 1)
assert(fib(9) == 34)
assert(fib(10) == 55)
assert(fib(50) == 12586269025)
assert(fib(100) == 354224848179261915075)



