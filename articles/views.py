from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def meat(request):
    return render(request, 'meat.html')

def dtl(request):
    name = 'JUNHA'
    context = {
        'name': name,
        'age' : 29,
        'foods' : ['고기', '회', '파전']
    }
    return render(request, 'dtl.html', context )

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    value = request.GET.get('search')
    name = 'junha'
    context = {
        'value' : value,
        'name' : name,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)