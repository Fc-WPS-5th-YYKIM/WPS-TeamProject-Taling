from rest_framework import serializers

from regiclass.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'curriculum_rate',
            'delivery_rate',
            'preparation_rate',
            'kindness_rate',
            'punctually_rate',
            'content',
            'modify_date',
        )