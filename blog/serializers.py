from rest_framework.serializers import ModelSerializer
from .models import BlogPost, BlogChannel, BlogComment


class BlogSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"


class ChannelSerializer(ModelSerializer):
    class Meta:
        model = BlogChannel
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"

