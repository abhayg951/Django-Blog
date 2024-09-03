from django.urls import path, include
from rest_framework import routers
from .admin.views import UserViewSet, UserProfileViewSet
from . import views

router = routers.DefaultRouter()
# user_list = UserViewSet.as_view()
router.register(r'users', UserViewSet)
router.register(r'users-profile', UserProfileViewSet)

urlpatterns = [
    path('admin/', include(router.urls)),
    path("api-auth", include('rest_framework.urls')),
    path("user", views.UserView.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        'patch': 'update'
    })),
]
