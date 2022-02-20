from rest_framework import serializers

from djangogram.users.models import User as user_model
from . import models


class FeedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = (
            "id",
            "username",
            "profile_photo",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Comment
        fields = (
            "id",
            "contents",
            "author",
        )


class PostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True)
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Post
        fields = (
            "id",
            "image",
            "caption",
            "comment_post",
            "author",
            "image_likes",
        )
