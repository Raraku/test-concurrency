"""airwave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from rest_framework import routers
from blog.viewsets import BlogPostViewSet, CommentViewSet, ChannelViewSet

router = routers.SimpleRouter()
router.register(r"posts", BlogPostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"channels", ChannelViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    re_path(".*", TemplateView.as_view(template_name="blog/build/index.html")),
]

