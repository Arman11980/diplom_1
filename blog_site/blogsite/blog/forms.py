from django import forms
from .models import Post, Comment

'''
Формы в Django позволяют пользователям вводить данные, которые затем могут быть обработаны и сохранены в базе данных
'''

#форма для регистрации
class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Ваш логин:')
    password = forms.CharField(min_length=8, label='Ваш пароль')
    repeate_password = forms.CharField(min_length=8, label='Повторите ваш пароль')
    age = forms.CharField(max_length=3, label='Ваш возраст')

#форма для поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'slug']

#форма для комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
