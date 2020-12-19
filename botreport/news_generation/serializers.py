from rest_framework import serializers


class LiveNewsSerializer(serializers.Serializer):
    text = serializers.CharField()
    data = serializers.CharField()
