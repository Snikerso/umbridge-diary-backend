from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet , UserProgressViewSet ,DormitorysViewSet

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'userprogress',UserProgressViewSet)
router.register(r'dormitorys', DormitorysViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
