from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(
        many=True,
        required=False,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('author', 'post',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    image = serializers.ImageField(required=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date',)
