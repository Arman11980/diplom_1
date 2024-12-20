"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from blog.views import sign_up_by_html

#Шаблоны URL’ов позволяют сопоставить адреса с обработчиками
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('new_post/', views.new_post, name='new_post'),
    path('<slug:slug>', views.post_details, name='post_details'),
    path('delete_blog_post/<slug:slug>/', views.delete_post,name='delete_blog_post'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # расположение статических и мультимедийных файлов

