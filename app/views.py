from django.shortcuts import render
from random import randint
# Create your views here.
def home(request):
    random_data = randint(1,99)
    print(random_data)
    context = {
        'data':"HELLO FROM DJANGO",
        'random':random_data
    }
    return render(request,'index.html',context)

def about(request):
    about = "WE ARE DEGREE CAMPUS"
    context = {
        'data':about
    }
    return render(request,'about.html',context)

def contact(request):
    contact = "Degree Campus, Biratnagar"
    context = {
        'data':contact
    }
    return render(request,'about.html',context)

def profile(request,username):
    print(username)
    context = {
        'username':username + " user"
    

    }
    return render(request,'profile.html',context)