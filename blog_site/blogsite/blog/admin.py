from django.contrib import admin
from .models import Post, Comment
'''
Панель администрирования позволяет изменять данные не используя код,
чтоб попасть в панель администрирования нужно зарегистрировать администратора командой в терминале
createsuperuser
'''
#добавление моделей на сайт администрирования
admin.site.register(Post)
admin.site.register(Comment)

