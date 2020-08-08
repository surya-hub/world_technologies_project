from django.shortcuts import render
from .forms import DemoRegisterForm
from django.core.mail import send_mail
from django.contrib import messages
from .models import Courses

def home(request):
    return render(request,'technology/home.html')



def DemoRegister(request):
    sent=False
    demoFrom=DemoRegisterForm()
    if request.method=='POST':
        data=DemoRegisterForm(request.POST)
        if data.is_valid():
            data.save()
            cd = data.cleaned_data
            subject = '{} ONLINE DEMO FROM WORLD TECHNOLOGIES Confirmation'.format(cd['course'])
            message = 'Dear {}\n\nThank you for Register {} online Demo our Admin will Contact you\n\n\n Thank you \n M.VENKATESH \n Human Resourse \n WORLD TECHNOLOGIES'.format( cd['first_name'], cd['course'])
            send_mail(subject, message, 'djangosuryatest@gmail.com', [cd['email']])
            sent = True
            messages.success(request, 'Thank you for register Email sent Successfully!!!')
    return render(request,'technology/demoRegister.html',{'form':demoFrom,'sent':sent})
def about(request):
    return render(request,'technology/about.html')

def services(request):
    courses=Courses.objects.all()

    return render(request,'technology/services.html',{'course':courses})

def Python_Content(request):
    courses=Courses.objects.all()

    return render(request,'technology/python_course.html',{'course':courses})