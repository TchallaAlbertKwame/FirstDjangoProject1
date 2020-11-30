from django.shortcuts import render, redirect
from .models import News
from .forms import RegistrationForm,RegistrationModal
from .models import RegistrationData
from  django.contrib import  messages


# Create your views here.

def Home(request):
    context = {
        "name": "Tchalla Albert Kwame"

    }
    return render(request, 'Home.html', context)


def Newsp(request):
    obj = News.objects.get(id=1)
    context = {
        "data": obj
    }
    return render(request, 'News.html', context)


def NewsDate(request, year):
    article_list = News.objects.filter(pub_date__year=year)
    context = {
        "year": year,
        "article_list": article_list
    }

    return render(request, 'newsdate.html', context)


def Contact(request):
    return render(request, 'Contact.html')


def Register(request):
    context = {
        "form": RegistrationForm

    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      Email=form.cleaned_data['Email'],
                                      Phone=form.cleaned_data['Phone'])
        myregister.save()
        messages.add_message(request,messages.SUCCESS, "You have successfully Sign Up !")
    return redirect('Register')


def modelform(request):
    context={
        "modalform":RegistrationModal

    }
    return render(request,'modalform.html',context)
