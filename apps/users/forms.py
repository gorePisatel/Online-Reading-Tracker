from django import forms

from .models import CustomUser, UserSettings


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "avatar",
            "bio",
        ]

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            UserSettings.objects.create(user=user)

        return user


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = UserSettings
        fields = [
            "theme",
            "is_private",
            "notifications_enabled",
        ]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "avatar",
            "bio",
        ]