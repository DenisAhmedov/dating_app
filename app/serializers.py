from geopy.distance import geodesic as GD

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.helpers import add_watermark
from app.models import Client


# class DistanceField(serializers.CharField):
#     def to_representation(self, value):
#         return '%s, %s' % (value.latitude, value.longitude)


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, required=True, write_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Client.objects.all())], required=False)
    distance = serializers.CharField(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'sex', 'password', 'avatar', 'latitude',
                  'longitude', 'distance']

    def create(self, validated_data):
        client = super().create(validated_data)

        client.set_password(client.password)
        if validated_data.get('avatar'):
            add_watermark(client.avatar)
        client.save()

        return client

    def update(self, instance, validated_data):
        client = super().update(instance, validated_data)

        client.set_password(client.password)
        if validated_data.get('avatar'):
            add_watermark(client.avatar)
        client.save()

        return client

    def to_representation(self, obj):
        old_repr = super().to_representation(obj)

        user = self.context['request'].user
        user_coord = (user.latitude, user.longitude)
        self_coord = (old_repr['latitude'], old_repr['longitude'])
        old_repr['distance'] = f'{int(GD(user_coord, self_coord).km)} km.'

        return old_repr

