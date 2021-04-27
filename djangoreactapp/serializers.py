from djangoreactapp.models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields =('id','taskname','handler')
