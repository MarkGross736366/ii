from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def chart(request):
    return render(request, 'chart.html')

def stock(request):
    return render(request, 'stock.html')

def ipo(request):
    return render(request, 'ipo.html')

def bank(request):
    return render(request, 'bank.html')

def book_list(request):
    return render(request, 'book_list.html')

def message_list(request):
    return render(request, 'message_list.html')
