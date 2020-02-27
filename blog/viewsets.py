from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import BlogSerializer, ChannelSerializer, CommentSerializer
from .models import BlogPost, BlogChannel, BlogComment


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = BlogChannel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [AllowAny]
