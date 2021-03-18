from rest_framework import serializers
from api.models import User, Author, Article


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = { "password": { "write_only" : True } }


    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1


    def create(self, validated_data, author_id):
        article = Article(**validated_data)
        article.author_id = author_id
        article.save()
        return article

