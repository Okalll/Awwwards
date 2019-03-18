from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .forms import SignupForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):

   return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            return render(request, 'profile.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    images = Image.objects.all()
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    posts = Image.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
        else:
            image_form = ProfileForm()

    return render(request, 'profile.html', {"image_form": image_form, "posts": posts, "profile": profile, "images": images})

