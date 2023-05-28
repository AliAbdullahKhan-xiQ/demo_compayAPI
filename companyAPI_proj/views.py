# function based vies
from django.http import HttpResponse


def home_page(request):
    print('Home page requested')  # return in terminal
    return HttpResponse("This is home page")
