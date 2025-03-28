from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profile', request.user.username)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', user.username)
        else:
            print("Username OR password is incorrect")

    return render(request, "users/login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('profile', user.username)


    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request, username):
    profile = Profile.objects.get(username=username)
    products = profile.product_set.all()
    context = {'profile': profile, 'products': products}
    return render(request, 'users/profile.html', context)
