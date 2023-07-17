from django_filters import rest_framework as filters

from app.models import Client


class ClientFilter(filters.FilterSet):
    """ Фильтрация участников по полу имени и фамилии """

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'sex']
