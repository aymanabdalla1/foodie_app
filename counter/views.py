from django.shortcuts import render

# Creating a view for the home page
def home(request):
    
    return render(request, 'home.html', {})

