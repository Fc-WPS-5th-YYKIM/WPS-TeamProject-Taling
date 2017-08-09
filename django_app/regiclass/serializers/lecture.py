from rest_framework import serializers

from regiclass.models import Lecture, ClassLocation, LecturePhoto


class ClassLocationSerializer(serializers.ModelSerializer):
    # location1 = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # location2 = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # location_option = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # location_detail = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # location_etc_type = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # location_etc_text = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # class_weekday = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # class_time = serializers.ListField(
    #     child=serializers.CharField(),
    # )

    class Meta:
        model = ClassLocation
        fields = (
            'location1',
            'location2',
            'location_option',
            'location_detail',
            'location_etc_type',
            'location_etc_text',
            'class_weekday',
            'class_time',
        )


class LecturePhotoSerializer(serializers.ModelSerializer):
    # photo_type = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # photo = serializers.ListField(
    #     child=serializers.CharField(),
    # )
    # description = serializers.ListField(
    #     child=serializers.CharField(),
    # )

    class Meta:
        model = LecturePhoto
        fields = (
            'photo_type',
            'photo',
            'description',
        )


class LectureListSerializer(serializers.ModelSerializer):
    locations = ClassLocationSerializer(many=True, read_only=True)
    lecture_photos = LecturePhotoSerializer(many=True, read_only=True)

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

            'locations',
            'lecture_photos',
        )
        read_only_fields = (
            'totur',
        )


class LectureMakeSerializer(serializers.ModelSerializer):
    location1 = serializers.ListField(
        child=serializers.CharField(),
    )
    location2 = serializers.ListField(
        child=serializers.CharField(),
    )
    location_option = serializers.ListField(
        child=serializers.CharField(),
    )
    location_detail = serializers.ListField(
        child=serializers.CharField(),
    )
    location_etc_type = serializers.ListField(
        child=serializers.CharField(),
    )
    location_etc_text = serializers.ListField(
        child=serializers.CharField(),
    )
    class_weekday = serializers.ListField(
        child=serializers.CharField(),
    )
    class_time = serializers.ListField(
        child=serializers.CharField(),
    )

    photo_type = serializers.ListField(
        child=serializers.CharField(),
    )
    photo = serializers.ListField(
        child=serializers.ImageField(),
    )
    description = serializers.ListField(
        child=serializers.CharField(),
    )

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

            'location1',
            'location2',
            'location_option',
            'location_detail',
            'location_etc_type',
            'location_etc_text',
            'class_weekday',
            'class_time',

            'photo_type',
            'photo',
            'description'
        )
        read_only_fields = (
            'lecture',
        )
