from django.shortcuts import render

def home(request):
    return render(request,'basicClassesAndForms/home.html',{'title' : 'Home'})
