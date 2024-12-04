from django.contrib import admin
from .models import Post, Comment

#добавление моделей на сайт администрирования
admin.site.register(Post)
admin.site.register(Comment)

