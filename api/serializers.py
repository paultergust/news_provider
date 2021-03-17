from rest_framework import serializers
from api.models import User, Author, Article


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = '__all__'


    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class AuthorSerializer(serializers.Serializer):

    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.Serializer):

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        article = Article(**validated_data)
        article.save()
        return article


    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.firstParagraph = validated_data.get('firstParagraph', instance.firstParagraph)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
