import time


# Create your models here.
def recursive_fib(self,input_number):
    if input_number <=1:
        return input_number
    else:
        return Fibonacci.recursive_fib(input_number-1) + Fibonacci.recursive_fib(input_number-2)
        

# using dynamic programming concept, avoid recalculation of already computed number 
# by storing the result
    
def fib(self,input_number):
    
    if input_number <=1:
        return input_number

    else:
        first = 0
        second = 1
        for i in range(2,input_number+1):
            third = first + second
            first = second
            second = third

        return third

#main_method
def multiply(F, M) : 
        
    x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]
    y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]
    z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]
    w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]
 
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n) :
    
    if( n == 0 or  n == 1):
        return;
    M = [[1,1],[1,0]];
 
    power(F, int(n/2))
    multiply(F, F)
 
    if (n%2 != 0):
        multiply(F, M)


def  mulplicative_fib(input_number):
    import sys
    sys.setrecursionlimit(1000000000)
    
    F = [[1,1],[1,0]];
    if (input_number == 0):
        return 0
        
    power(F, input_number-1)
    return F[0][0]




    
 


    
    