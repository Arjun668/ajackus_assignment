from django.urls import path
from rest_framework import routers

from api.cms.views import Category, ContentViewset

app_name = 'cms'

router = routers.SimpleRouter()
router.register('content', ContentViewset)

urlpatterns = router.urls
