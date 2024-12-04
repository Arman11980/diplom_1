from django.db import models
from django.contrib.auth.models import User #аунтификация пользователей
from django.template.defaultfilters import slugify

#модель для поста
class Post(models.Model):
    title = models.CharField(max_length=150, unique=True) #заголовок статьи
    author = models.ForeignKey(User, on_delete=models.CASCADE) #внешний ключ один ко многим
    slug = models.SlugField(max_length=100, unique=True) # URL-статьи
    body = models.TextField() # содержание статьи
    image = models.ImageField(upload_to="images/", blank=True, null=True) #загрузка изображений
    created_on = models.DateTimeField(auto_now_add=True) #дата создания статьи
    updated_on = models.DateTimeField(auto_now=True) #дата внесения изменений статьи

    class Meta: #метаданные(сортировка статей) в порядке убывания
        ordering = ['-created_on']

    def __str__(self):
        return self.title #возвращает отображение понятное для человека

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

# модель комментариев к посту кем и когда создан
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
