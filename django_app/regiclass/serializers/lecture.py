from django.db.models import Sum, Avg
from rest_framework import serializers

from regiclass.models import Lecture, ClassLocation, LecturePhoto
from regiclass.serializers import ReviewSerializer

__all__ = (
    'ClassLocationSerializer',
    'LecturePhotoSerializer',
    'LectureListSerializer',
    'LectureMakeSerializer',

)


class ClassLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLocation
        fields = (
            'id',
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
    class Meta:
        model = LecturePhoto
        fields = (
            'id',
            'photo_type',
            'photo',
            'description',
        )


class LectureListSerializer(serializers.ModelSerializer):
    locations = ClassLocationSerializer(many=True, read_only=True)
    lecture_photos = LecturePhotoSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Lecture
        fields = (
            'id',
            'tutor',
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
            'like_users',
            'state',
            'modify_date',

            'locations',
            'lecture_photos',
            'reviews'
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        user = self.context['user']
        if user.is_authenticated:
            ret['is_like'] = instance.likelecture_set.filter(user=user, lecture=instance.id).exists()
        ret['like_count'] = instance.likelecture_set.count()
        ret['review_count'] = instance.reviews.count()
        ret['review_average'] = instance.reviews.filter(lecture=instance.id).aggregate(
            curriculum_rate=Avg('curriculum_rate'),
            delivery_rate=Avg('delivery_rate'),
            preparation_rate=Avg('preparation_rate'),
            kindness_rate=Avg('kindness_rate'),
            punctually_rate=Avg('punctually_rate')
        )
        ret['review_sum'] = instance.reviews.filter(lecture=instance.id).aggregate(
            curriculum_rate=Sum('curriculum_rate'),
            delivery_rate=Sum('delivery_rate'),
            preparation_rate=Sum('preparation_rate'),
            kindness_rate=Sum('kindness_rate'),
            punctually_rate=Sum('punctually_rate')
        )
        ret['tutor_info'] = {
            'nickname': instance.tutor.author.nickname,
        }
        return ret


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

    def save(self, tutor, **kwargs):
        lecture, lecture_created = Lecture.objects.get_or_create(
            tutor=tutor,
            title=self.validated_data['title'],
            category=self.validated_data['category'],
            class_type=self.validated_data['class_type'],
            min_member=self.validated_data['min_member'],
            max_member=self.validated_data['max_member'],
            cover_photo=self.validated_data['cover_photo'],
            tutor_intro=self.validated_data['tutor_intro'],
            class_intro=self.validated_data['class_intro'],
            target_intro=self.validated_data['target_intro'],
            price=self.validated_data['price'],
            basic_class_time=self.validated_data['basic_class_time'],
            total_count=self.validated_data['total_count'],
            youtube_url1=self.validated_data['youtube_url1'],
            youtube_url2=self.validated_data['youtube_url2'],
            region_comment=self.validated_data['region_comment'],
            notice=self.validated_data['notice'],
        )

        if lecture_created:
            for i in range(len(self.validated_data['location1'])):
                ClassLocation.objects.get_or_create(
                    lecture=lecture,
                    location1=self.validated_data['location1'][i],
                    location2=self.validated_data['location2'][i],
                    location_option=self.validated_data['location_option'][i],
                    location_detail=self.validated_data['location_detail'][i],
                    location_etc_type=self.validated_data['location_etc_type'][i],
                    location_etc_text=self.validated_data['location_etc_text'][i],
                    class_weekday=self.validated_data['class_weekday'][i],
                    class_time=self.validated_data['class_time'][i],
                )

            for j in range(len(self.validated_data['photo_type'])):
                LecturePhoto.objects.get_or_create(
                    lecture=lecture,
                    photo_type=self.validated_data['photo_type'][j],
                    photo=self.validated_data['photo'][j],
                    description=self.validated_data['description'][j],
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
