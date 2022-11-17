from rest_framework import serializers

from main.models import Ad, Rubric, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    rubric = RubricSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


