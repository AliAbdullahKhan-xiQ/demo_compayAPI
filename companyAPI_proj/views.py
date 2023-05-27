# function based vies
from django.http import HttpResponse # need to import this library for httpresponse.


def home_page(request):
    print('Home page requested') # return in terminal
    return HttpResponse("This is home page")
