from rest_framework import serializers


class SignupSerizlizer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    terms = serializers.BooleanField(required=True)
    password = serializers.CharField(min_length=8, max_length=16,
                                     required=True)
  