from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username = username,
                password = password
            )
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()

        args = {'form': form}

        return render(request, 'registration/register.html', args)
  
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)   
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/view_profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('view_profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'registration/change-password.html', args)


