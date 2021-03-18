from rest_framework import permissions
from rest_framework.authtoken.models import Token

from api.models import User

class AdminAuthentication(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            token = request.headers['token']
        except:
            token = ''

        token_query = Token.objects.filter(key=request.headers['token']).first()
        user = token_query.user
        return user.is_admin
