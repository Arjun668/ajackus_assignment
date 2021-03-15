from rest_framework import status, viewsets

from django.contrib.auth.models import Group
from rest_framework.permissions import AllowAny

from api.account.models import User
from api.account.serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = response.data
            # Set user group
            author_group = Group.objects.get(name='Author')
            author_group.user_set.add(user['id'])
        return response
