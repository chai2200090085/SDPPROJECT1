from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import string
import random
from .forms import *


def carcards(request):
    return render(request,'cards.html')
def hello1(request):
    return HttpResponse("<center><h1>Welcome to ttm Homepage<h1></center>")
def newhomepage(request):
    return render(request,'NewHomepage.html')
def travelpackage(request):
    return render(request,'travelpackage123.html')
def print1(request):
    return render(request,'print_to_console.html')
def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input': user_input}
    return render(request,'print_to_console.html',a1)
def randomcall(request):
    return render(request,'randomotpgenerator.html')
def randomlogic(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input:{user_input}')
        a2=int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1={'ran1': ran1}
    return render(request,'randomotpgenerator.html',a1)
def getdate1(request):
    return render(request,'dattime.html')
import datetime
from django.shortcuts import render
def dattime(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'dattime.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
            return render(request,'dattime.html',{'form':form})
from .models import *
from django.shortcuts import render,redirect
def register(request):
    return render(request,'Registerpage.html')
def Registerpage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            return HttpResponse("EMAIl already registered choose a different email")
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('NewHomepage')
    return render(request,'Registerpage.html')
import matplotlib.pyplot as plt
import numpy as np
def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'pie_chart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'pie_chart.html', {'form': form})
import requests
def weatherpagecall(request):
    return render(request,'weatherappinput.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '9d4d78470131c605bc299ae77bb971a0'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
    return render(request,'loginpage.html')
def signup(request):
    return render(request,'signuppage.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user= auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewHomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'loginpage.html')
    else:
        return render(request,'loginpage.html')

def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signuppage.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'loginpage.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signuppage.html')
def logout(request):
    auth.logout(request)
    return render (request,'NewHomepage.html')
def Feedbackcall(request):
    return render(request,'Feedbackform.html')

from.models import*
from django.shortcuts import render,redirect
def Feedbackform(request):
    if request.method == 'POST':
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        Email = request.POST.get('Email')
        Comments = request.POST.get('Comments')
        tosend=f'{Firstname} {Lastname}, Thank you for your feedback!'
        Feedbackformde.objects.create(Firstname=Firstname, Lastname=Lastname, Email=Email, Comments=Comments )
        send_mail(
            'Thank You for Contacting chaitanyas Travel Tourism and Managment ',
        tosend,
        '220009085csit@gmail.com',
        [Email],
        fail_silently = False,
        )
        return redirect('NewHomepage')

    return render(request, 'Feedbackform.html')