from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .forms import SignupForm, ProfileForm, ProjectForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):

   return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            return render(request, 'registration/login.html/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    images = Profile.objects.all()
    current_user = request.user
    profile = Profile.objects.all()
    posts = Profile.objects.all()
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
        else:
            image_form = ProfileForm()

    return render(request, 'profile.html', {"image_form": image_form, "profile": profile, "images": images})

def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.poster = current_user
            projects.save()
        return redirect('home')

    else:
        form = ProjectForm()
    return render(request, 'upload.html', {"form": form })

@login_required(login_url='/accounts/login/')
def project(request,project_id):
   projects = Projects.objects.get(id=project_id)
   rating = round(((project.design + project.usability + project.content)/3),2)
   if request.method == 'POST':
       form = VoteForm(request.POST)
       if form.is_valid:
           project.vote_submissions += 1
           if project.design == 0:
               project.design = int(request.POST['design'])
           else:
               project.design = (project.design + int(request.POST['design']))/2
           if project.usability == 0:
               project.usability = int(request.POST['usability'])
           else:
               project.usability = (project.design + int(request.POST['usability']))/2
           if project.content == 0:
               project.content = int(request.POST['content'])
           else:
               project.content = (project.design + int(request.POST['content']))/2
           project.save()
           return redirect(reverse('project',args=[project.id]))
   else:
       form_ = VoteForm()
   return render(request,'project.html',{'form_':form_,'projects':projects,'rating':rating})
