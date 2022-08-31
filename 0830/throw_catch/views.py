from django.shortcuts import render

# Create your views here.

def first(request):
    throw = '아무것도 받지 못함'
    throw = request.GET.get('secondthrow')
    context = {
        'throw': throw
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    throw = request.GET.get('firstthrow')
    context = {
        'throw': throw
    }

    return render(request, 'throw_catch/second.html', context)

