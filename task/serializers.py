import datetime

from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            "created_at": {"read_only": True},
            "start_date": {"read_only": True},
            "end_date": {"read_only": True}
        }

    def update(self, instance, validated_data):
        success = validated_data.get('success', None)
        # Без часового пояса
        if success is not None:
            validated_data['end_date'] = datetime.datetime.now()
        return super().update(instance, validated_data)


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name',)

    @property
    def data(self):
        return ReturnDict(TaskSerializer(self.instance).data, serializer=TaskSerializer)
