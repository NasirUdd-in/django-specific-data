from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from .serializers import AuthorSerializer, PostSerializer
from .models import Author, Post, UserProfile

from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileForm, CustomUserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout

# Create your views here.
class ListAuthorAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CreateAuthorAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class UpdateAuthorAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class DeleteAuthorAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def members(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/api/details/')  # Redirect to your desired view
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/api/details/')  # Redirect to your desired view
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def my_details(request):
    try:
        user_details = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Handle the case where the user profile does not exist
        user_details = None
    
    context = {'user_details': user_details}
    return render(request, 'details.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('login') 