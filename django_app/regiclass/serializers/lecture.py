from rest_framework import serializers

from regiclass.models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    # Field 의 source 인자는 어떤 속성으로 Field 를 생성할 지 결정해준다.
    # 직렬화된 인스턴스의 속성을 가리킬 수 있으며 읽기 전용이기 때문에 serialize 된 표현으로 사용 가능하지만,
    # deserialize 후 업데이트에는 사용되지 못 한다.

    class Meta:
        model = Lecture
        fields = ('id', 'title', 'category', '[...]', 'owner',)
