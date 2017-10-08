from django.conf.urls import include, url
from rest_framework import routers

from cube import views

router = routers.SimpleRouter()
router.register(r'cube', views.CubeViewSet, 'cube')

urlpatterns = [
    url(r'^', include(router.urls)),
]
