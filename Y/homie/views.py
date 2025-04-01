from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Lander.html')

def page1(request):
    return render(request, 'dashboard.html')