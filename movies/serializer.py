from rest_framework import serializers
from movies.models import RatingChoices, Movie
from users.serializer import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(
        default=None,
        allow_null=True,
    )
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, default=RatingChoices.G, allow_null=True
    )
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
