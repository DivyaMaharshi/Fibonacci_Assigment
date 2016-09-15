from django.shortcuts import render_to_response
from Project1_Fibonacci import Fibonacci
import time


# Create your views here.

def homepage(request):
    return render_to_response("Project1_Fibonacci/homepage.html")

def fibonacci_response(request):
    start1 = time.time()
    input_number = request.GET['number']
    
    if input_number !='' and int(input_number) >= 0:
        
        #result_recursivefib = Fibonacci.fib(int(input_number))
        #result_recursivefib = Fibonacci.recursive_fib(int(input_number))
        result_fib = Fibonacci.mulplicative_fib(int(input_number))
        
        #import pdb;pdb.set_trace()
        timetaken_fib = round((time.time() - start1),4)
        return render_to_response("Project1_Fibonacci/extend_homepage.html",
                                                        {"entered_number": input_number,
                                                        "result_fib":result_fib,
                                                        'timetaken_fib':timetaken_fib,
                                                        })
    else:
        return render_to_response("Project1_Fibonacci/homepage.html")


