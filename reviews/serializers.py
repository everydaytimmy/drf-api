from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "reviewer", "title", "body", "created_at")
        model = Review