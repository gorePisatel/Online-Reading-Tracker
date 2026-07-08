from django.forms import (
    ModelForm,
    CharField,
    PasswordInput,
    ValidationError,
)

from .models import CustomUser, UserSettings


class RegistrationForm(ModelForm):
    password1 = CharField(widget=PasswordInput())
    password2 = CharField(widget=PasswordInput())

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'password1',
            'password2',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError('Passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
            UserSettings.objects.get_or_create(user=user)

        return user


class UserSettingsForm(ModelForm):

    class Meta:
        model = UserSettings
        fields = [
            'theme',
            'is_private',
            'notifications_enabled',
        ]


class UserUpdateForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'avatar',
            'bio',
        ]
