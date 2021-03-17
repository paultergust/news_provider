from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from api.serializers import UserSerializer, ArticleSerializer
from api.models import Article
from api.permissions import AdminAuthentication

# Create your views here.

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.create(data)
        token = Token.objects.get(user=user)
        response = {"username": user.username, "token":str(token)}
        return Response(response, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def articles(request):
    token = request.headers['token']
    data = {}
    try:
        category = request.query_params['category']
        articles = Article.objects.filter(category=category)
    except:
        articles = Article.objects.all()
    finally:
        data = ArticleSerializer(articles).data

    if valid_token(token):
        return Response(data)

    return Response(data.errors)


class ArticlesCrud(ListAPIView):
    permission_classes=[AdminAuthentication,]

    def get(self, request):
        articles = Article.objects.all()
        data = ArticleSerializer(articles).data
        return Response(data)


def valid_token(token):
    aux_token = Token.objects.filter(key=token)[0]
    return str(aux_token) == token

