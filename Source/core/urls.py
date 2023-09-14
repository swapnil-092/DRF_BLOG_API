from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('api/user/', include('user.urls', namespace='user')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('blog.urls', namespace='blog')),

]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls', namespace='blog')),
#     path('api/', include('blog_api.urls', namespace='blog_api')),
#     path('api/user/', include('user.urls', namespace='user')),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]