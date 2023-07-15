from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Client
from app.serializers import UserCreateSerializer


class ClientCreateView(CreateAPIView):
    model = Client
    serializer_class = UserCreateSerializer


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

