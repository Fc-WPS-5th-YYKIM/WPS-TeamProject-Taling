from rest_framework import serializers

from regiclass.models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            'title',
            'category',
            'class_type',
            'min_member',
            'max_member',
            'cover_photo',
            'tutor_intro',
            'class_intro',
            'target_intro',
            'price',
            'basic_class_time',
            'total_count',
            'youtube_url1',
            'youtube_url2',
            'region_comment',
            'notice',
        )
        read_only_fields = (
            'totur',
        )
