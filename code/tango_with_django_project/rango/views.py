from django.shortcuts import HttpResponse, render

def index(request):
    context_dict = { "boldmessage": "I am bold font from the context"}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {"aboutmessage": "This is the about page."}

    return render(request, 'rango/about.html', context_dict)
