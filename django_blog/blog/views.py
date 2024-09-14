from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})
    
class LoginView(LoginView):
    template_name = "login.html"

def product(request):
    return render(request, "product.html")

def index(request):
    return render(request, "index.html")