from django.shortcuts import render, redirect
from movies.forms import registerform, UserupdateForm, ProfileupdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


def registeruser(request):

    form = registerform()

    if request.method == "POST":
        form = registerform(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(
                request, f'account for {username} has been successfully created')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/registeruser.html', context)
    else:
        return render(request, 'accounts/registeruser.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserupdateForm(request.POST, instance=request.user)
        p_form = ProfileupdateForm(
            request.POST, request.FILES,  instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile succesfully updated')
            return redirect('home')

    else:
        u_form = UserupdateForm(instance=request.user)
        p_form = ProfileupdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form

        }
        return render(request, 'accounts/profile.html', context)
