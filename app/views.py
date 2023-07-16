from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Client
from app.permissions import IsClientOrAdmin
from app.serializers import ClientSerializer


class ClientCreateView(CreateAPIView):
    model = Client
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]


class GetAllClients(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsClientOrAdmin]


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
