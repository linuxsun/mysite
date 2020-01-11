from rest_framework import serializers
from .models import VideoDetails,Video


class VideoDetailsSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(source='get_absolute_image_url', read_only=True)

    class Meta:
        model = VideoDetails
        fields = ('video', 'image_url')



class VideoSerializer(serializers.ModelSerializer):
    video_details = VideoDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        # fields = '__all__'
        fields = ('title','details','video_details')




