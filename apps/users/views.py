from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegistrationForm, UserUpdateForm, UserSettingsForm


def register_view(request):

    if request.method == "POST":

        form = RegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Registration successful."
            )

            return redirect("profile")

    else:
        form = RegistrationForm()

    return render(
        request,
        "users/register.html",
        {
            "form": form
        }
    )


@login_required
def profile_view(request):

    return render(
        request,
        "users/profile.html",
        {
            "user": request.user
        }
    )


@login_required
def settings_view(request):

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        settings_form = UserSettingsForm(
            request.POST,
            instance=request.user.settings
        )

        if user_form.is_valid() and settings_form.is_valid():

            user_form.save()
            settings_form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        settings_form = UserSettingsForm(
            instance=request.user.settings
        )

    return render(
        request,
        "users/base.html",
        {
            "user_form": user_form,
            "settings_form": settings_form,
        }
    )