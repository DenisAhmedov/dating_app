from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.helpers import add_watermark
from app.models import Client


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, required=True, write_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Client.objects.all())], required=False)

    class Meta:
        model = Client
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'sex', 'password', 'avatar']

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



