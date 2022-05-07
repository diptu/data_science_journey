from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_veiw(request):
    return render(request, 'home.html')

def about_veiw(request):
    return render(request, 'about.html')

def contact_veiw(request):
    return HttpResponse("<h1>Hello</h1>")