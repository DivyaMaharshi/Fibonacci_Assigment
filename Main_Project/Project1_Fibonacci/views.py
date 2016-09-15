from django.shortcuts import render_to_response
from Project1_Fibonacci.models import Fibonacci
import time


# Create your views here.

def homepage(request):
    return render_to_response("Project1_Fibonacci/homepage.html")

def fibonacci_response(request):
    start = time.time()
    input_number = request.GET['number']
    input_number = int(input_number)

    if input_number != '' and input_number > 0 :
            result = Fibonacci.fib(input_number)
            return render_to_response("Project1_Fibonacci/extend_homepage.html",{"entered_number": input_number, "fibonacci_number":result,'timetaken':round((time.time() - start),4)})

    else:
        return render_to_response("Project1_Fibonacci/homepage.html")


