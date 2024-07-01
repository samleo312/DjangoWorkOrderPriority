from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResourceViewSet, UnaddedWorkOrderViewSet, AddedWorkOrderViewSet

router = DefaultRouter()
router.register(r'resources', ResourceViewSet, basename='resource')
router.register(r'unaddedworkorders', UnaddedWorkOrderViewSet, basename='unaddedworkorder')
router.register(r'addedworkorders', AddedWorkOrderViewSet, basename='addedworkorder')

urlpatterns = [
    path('', include(router.urls)),
]
