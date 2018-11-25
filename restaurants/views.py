from django.shortcuts import render

from django.http import HttpResponse

def fun(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'file.html', context)
