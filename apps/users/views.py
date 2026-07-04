from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistrationForm, UserSettingsForm, UserUpdateForm
from .models import UserSettings


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("profile")

        messages.error(request, "Please fix the errors below.")
    else:
        form = RegistrationForm()

    return render(
        request,
        "users/register.html",
        {
            "form": form,
        },
    )


@login_required
def profile_view(request):
    user_settings, _ = UserSettings.objects.get_or_create(user=request.user)

    return render(
        request,
        "users/profile.html",
        {
            "user_settings": user_settings,
        },
    )


@login_required
def settings_view(request):
    user_settings, _ = UserSettings.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )
        settings_form = UserSettingsForm(
            request.POST,
            instance=user_settings,
        )

        if user_form.is_valid() and settings_form.is_valid():
            user_form.save()
            settings_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")

        messages.error(request, "Please fix the errors below.")
    else:
        user_form = UserUpdateForm(instance=request.user)
        settings_form = UserSettingsForm(instance=user_settings)

    return render(
        request,
        "users/settings.html",
        {
            "user_form": user_form,
            "settings_form": settings_form,
        },
    )
