from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['firstname'] = user.first_name
        token['username'] = user.username

        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class PostSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Post
        fields = ["id", "author", "title", "body", "created", "status", "updated", "is_published", "is_active"]


'''
./manage.py shell

from posts.models import Post
from api.serializers import PostSerializer
posts = Post.objects.all()
serializer = PostSerializer(posts, many=True)
serializer.data
>>> 
'''
