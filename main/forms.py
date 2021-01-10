from django import forms
from .models import Blog, Search, Person, Biography, Email, DreamRubric, Comment

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.validators import FileExtensionValidator


class BlogForm(forms.ModelForm):
    title = forms.CharField(label = 'Заголовок')
    text = forms.CharField(label = 'Текст')
    image = forms.ImageField(label = 'Изображение', validators = [FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], error_messages={'invalid_extension': 'Этот формат не поддерживается.'}, required = False)
    
    class Meta:
        model = Blog
        fields = ('title', 'text', 'image',)
        
        
class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label = '')
    
    class Meta:
        model = Comment
        fields = ('comment_text',)
        

class SearchForm(forms.ModelForm):
    search_field = forms.CharField(label = '', required = False)
    
    class Meta:
        model = Search
        fields = ('search_field',) 
        
        
class BiographyForm(forms.ModelForm):
    bio = forms.CharField(label = "Опишите себя", error_messages={'required': 'О себе'})
    dream = forms.CharField(label = "Мечта", error_messages={'required': 'Ваша мечта'})
    dreamrubric = forms.ModelChoiceField(queryset = DreamRubric.objects.all(), label = "Категория", empty_label = None, error_messages={'required': 'Выберите категорию'}, widget=forms.widgets.Select(attrs={'size': 8}))
    #Походу надо всетаки создать модель dreamrubric и связать её 
    
    class Meta:
        model = Biography
        fields = ('bio', 'dream', 'dreamrubric',)
        
        
class EmailForm(forms.ModelForm):
    email = forms.EmailField(label = "", error_messages={'required': 'Указать почту'})
    
    class Meta:
        model = Email
        fields = ('email',)