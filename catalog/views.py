from django.shortcuts import render

<<<<<<< HEAD
def home_view(request):
    return render(request, 'catalog/home.html')

def contacts_view(request):
    return render(request, 'catalog/contacts.html')
=======
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

>>>>>>> d9679e90beb07769dcace178c687f635124c8a43
