from django.contrib.auth import authenticate
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    CharField,
    EmailField,
    ValidationError,
)

from apps.users.models import CustomUser, UserSettings


class UserReadSerializer(ModelSerializer):
    theme = SerializerMethodField()
    is_private = SerializerMethodField()
    notifications_enabled = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'bio',
            'role',
            'theme',
            'is_private',
            'notifications_enabled',
        ]
        read_only_fields = [
            'id',
            'email',
            'role',
            'theme',
            'is_private',
            'notifications_enabled',
        ]

    def get_theme(self, obj):
        settings = getattr(obj, 'settings', None)
        return settings.theme if settings else None

    def get_is_private(self, obj):
        settings = getattr(obj, 'settings', None)
        return settings.is_private if settings else None

    def get_notifications_enabled(self, obj):
        settings = getattr(obj, 'settings', None)
        return settings.notifications_enabled if settings else None


class UserRegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(
            password=password,
            **validated_data,
        )
        UserSettings.objects.get_or_create(user=user)
        return user


class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get('request'),
            username=attrs.get('email'),
            password=attrs.get('password'),
        )

        if not user:
            raise ValidationError('Invalid email or password.')

        if not user.is_active:
            raise ValidationError('User account is disabled.')

        attrs['user'] = user
        return attrs
