from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("""Rango says hello world!
        <br/><a href=\"/rango/about\">About us</a>""")

def about(request):
    return HttpResponse("""Rango says this is the about page.
        <br/><a href=\"/rango\">Home</a>""")
