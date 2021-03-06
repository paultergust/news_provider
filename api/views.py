from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from api.serializers import UserSerializer, ArticleSerializer, AuthorSerializer
from api.models import Article, Author
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


#check request token validity
def valid_token(request):
    try:
        token = request.headers['token']
        aux_token = Token.objects.filter(key=token)[0]
    except:
        return False
    return str(aux_token) == token


@api_view(['GET'])
def articles(request):
    try:
        category = request.query_params['category']
        articles = Article.objects.filter(category=category)
    except:
        articles = Article.objects.all()

    if valid_token(request):
        data = ArticleSerializer(articles, many=True, anonymous=False).data
        return Response(data)
    else:
        data = ArticleSerializer(articles, many=True, anonymous=True).data
        return Response(data)


# ADMIN/ARTICLES CLASS VIEW
class ArticlesList(APIView):
    permission_classes = [AdminAuthentication,]

    def get(self, request):
        objs = Article.objects.all()
        data = ArticleSerializer(objs, many=True).data
        return Response(data)


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        try:
            author_id = request.data['author_id']
        except:
            return Response(serializer.errors, status=400)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        serializer.create(request.data, author_id)
        return Response(serializer.data, status=201)

    
class ArticleView(APIView):
    permission_classes = [AdminAuthentication,]

    def patch(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        serializer.update(article, request.data)
        return Response(serializer.data, status=200)


    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=204)
        

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
            

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=400)


# ADMIN/AUTHORS CLASS VIEW
class AuthorsList(APIView):
    permission_classes = [AdminAuthentication,]

    def get(self, request):
        objs = Author.objects.all()
        data = AuthorSerializer(objs, many=True).data
        return Response(data)


    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        serializer.save()
        return Response(serializer.data, status=201)

    
class AuthorView(APIView):
    permission_classes = [AdminAuthentication,]

    def patch(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        serializer.update(author, request.data)
        return Response(serializer.data, status=200)


    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=204)
        

    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
            

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=400)

