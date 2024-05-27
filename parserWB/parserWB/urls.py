"""
URL configuration for parserWB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from parserWBapp.api_views import PostViewSet, ProductViewSet,  TagViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'products', ProductViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categorys', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('parserWBapp.urls', namespace='parsing')),
    path('user/', include('userapp.urls', namespace='user')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v0/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns = [
#         path("__debug__/", include("debug_toolbar.urls")),
# ] + urlpatterns