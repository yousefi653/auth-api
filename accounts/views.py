from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from . import serilizers


# Create your views here.
class Register(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serilizers.RegisterSer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            email = user.email
            first_name = user.fisrt_name
            last_name = user.last_name
            return Response(
                data={
                    "message": "User registered successfully",
                    "user": {
                        "email": email,
                        "first_name": first_name,
                        "last_name": last_name,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"message": "not registerd", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class Login(TokenObtainPairView):
    serializer_class = serilizers.CustomTokenObtainPairSer


class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response(
                data={"message": "refresh token is required!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "logout successfuly!"}, status=status.HTTP_205_RESET_CONTENT
            )
        except TokenError:
            return Response(
                {"message": "logout failed!", "error": TokenError},
                status=status.HTTP_400_BAD_REQUEST,
            )


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(
            data={
                "message": "info",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone": user.phone,
                },
            }
        )
