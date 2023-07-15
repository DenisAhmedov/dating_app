from rest_framework import serializers

from app.models import Client


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, required=True, write_only=True)

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'email', 'sex', 'password']

    def create(self, validated_data):
        client = super().create(validated_data)

        client.set_password(client.password)
        client.save()

        return client

