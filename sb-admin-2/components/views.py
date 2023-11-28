from django.shortcuts import render

# Create your views here.

def home(request):
    "Function for testing all the template components"
    return render(request, 'components/home.html')
