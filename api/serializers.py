from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('created',)


# Just another one variant of validation!!! )))
# 
# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(slug_field='username', read_only=True)
#     following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

#     class Meta:
#         fields = '__all__'
#         model = Follow

#     def validate_following(self, value):
#         following = Follow.objects.filter(
#             user=self.context['request'].user,
#             following__username=self.context['request'].data['following']
#             ).all()
#         if following.exists():
#             raise serializers.ValidationError('Вы уже подписаны на этого автора.')
#         return value


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', default=serializers.CurrentUserDefault(), read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]
