from rest_framework import serializers
from restapp.models import Course

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model= Course
        field = (
            'id',
            'Name',
            'Description',
            'Published'
        )