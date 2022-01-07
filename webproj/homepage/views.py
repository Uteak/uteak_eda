from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    dic = {}
    return render(request, 'index.html', dic)

def head(request):
    dic = {}
    return render(request, 'eda_head2.html', dic)

def see(request):
    dic = {}
    return render(request, 'eda_see.html', dic)

def result1(request):
    dic = {}
    return render(request, 'eda_result1.html', dic)

def result2(request):
    dic = {}
    return render(request, 'eda_result2.html', dic)

