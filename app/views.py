from math import cos, radians

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters


from app.filters import ClientFilter
from app.helpers import send_mail_to_matched
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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClientFilter

    def get_queryset(self):
        try:
            distance = float(self.request.GET.get('distance'))
            my_longitude = self.request.user.longitude
            my_latitude = self.request.user.latitude
            lon1 = my_longitude - distance / abs(cos(radians(my_latitude)) * 111.0)
            lon2 = my_longitude + distance / abs(cos(radians(my_latitude)) * 111.0)
            lat1 = my_latitude - (distance / 111.0)
            lat2 = my_latitude + (distance / 111.0)
            queryset = Client.objects.filter(latitude__range=(lat1, lat2))\
                .filter(longitude__range=(lon1, lon2))\
                .exclude(pk=self.request.user.id)
            return queryset
        except TypeError:
            queryset = Client.objects.all()
            return queryset


class ClientView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsClientOrAdmin]


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class MatchView(APIView):
    def post(self, request, pk):
        client = Client.objects.get(pk=pk)

        if client not in request.user.who_likes.all():
            request.user.who_likes.add(client)
            if request.user in client.who_likes.all():
                send_mail_to_matched(
                    (client.full_name, client.email),
                    (request.user.full_name, request.user.email)
                )
                return Response({'email': client.email}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


