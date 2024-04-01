from django.shortcuts import render
from random import randint
# Create your views here.
from .models import  Person,Gender
def list_donors(request):
    donor_person = Person.objects.all()
    adult_donors = Person.objects.filter(age=18)
    
    male = Gender.objects.get(id=1)
    male_count = Person.objects.filter(gender=male).count()

    print("Adult: ",adult_donors)
    total_donors = donor_person.count()
    print("TOTAL PERSON : ",total_donors )
    for person in donor_person:
        print(person.name)
        print(person.blood_group)
        print(person.age)
        print("______")

    context = {

    }
    return render(request,'list_donors.html',context)

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
    users = [
        {
            'username':'ram',
            'full_name':"Ram Kumar Thapa",
            'designation':"Web Developer",
        }
        ,
        {
            'username':'hari',
            'full_name':"Hari Kumar Thapa",
            'designation':"App Developer",
        },
        {
            'username':'shyam',
            'full_name':"Shyam  Thapa",
            'designation':"Python Developer",
        }
    ]
    found_user = None
    for user in users:
        print(user['username'])
        if user['username'] == username:
            found_user = user
    context = {
        'username':username + " user",
        'users':users,
        'found_user':found_user
    }
    return render(request,'profile.html',context)