from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.cms.models import Category, Content
from api.cms.serializers import CategorySerializer, ContentSerializer

from api.cms.utils import is_admin_user


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContentViewset(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        search_keyword = request.GET.get('search_keyword')

        # We have 2 types of user 1. Admin and 2. Author.
        # Admin can see all author's contents but Author can see his content only
        if not is_admin_user(request):
            # For Author
            self.queryset = self.get_queryset().filter(user_id=request.user.id)

        # Perform search for content if search keyword exist
        if search_keyword:
            self.queryset = self.get_queryset().filter(
                Q(title__icontains=search_keyword) | Q(body__icontains=search_keyword) |
                Q(summary__icontains=search_keyword) | Q(category__category_name__icontains=search_keyword)
            )

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        # Set logged in user at creation for content.
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)




