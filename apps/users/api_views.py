from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import (
    LoginSerializer,
    UserReadSerializer,
    UserRegisterSerializer,
)


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                UserReadSerializer(user, context={'request': request}).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'token': token.key,
                    'user': UserReadSerializer(
                        user,
                        context={'request': request},
                    ).data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            {'detail': 'Logged out successfully.'},
            status=status.HTTP_200_OK,
        )


class PersonalInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserReadSerializer(
            request.user,
            context={'request': request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = UserReadSerializer(
            request.user,
            data=request.data,
            partial=True,
            context={'request': request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
