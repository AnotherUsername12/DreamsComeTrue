from django import forms
from .models import Blog, Search, Person, Biography, Email, DreamRubric, Comment

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.validators import FileExtensionValidator


class BlogForm(forms.ModelForm):
    title = forms.CharField(label = 'Header')
    text = forms.CharField(label = 'Text')
    image = forms.ImageField(label = 'Image', validators = [FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], error_messages={'invalid_extension': 'This format is not supported.'}, required = False)
    
    class Meta:
        model = Blog
        fields = ('title', 'text', 'image',)
        
        
class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label = '', widget=forms.widgets.Textarea())
    
    class Meta:
        model = Comment
        fields = ('comment_text',)
        

class SearchForm(forms.ModelForm):
    search_field = forms.CharField(label = '', required = False)
    
    class Meta:
        model = Search
        fields = ('search_field',) 
        
        
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter your username', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter your password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Nickname already taken")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password mismatch")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1']
        )
        return user
    
        
        
class BiographyForm(forms.ModelForm):
    bio = forms.CharField(label = "Describe yourself", error_messages={'required': 'About'}, widget=forms.widgets.Textarea())
    dream = forms.CharField(label = "Dream", error_messages={'required': 'Your dream'})
    dreamrubric = forms.ModelChoiceField(queryset = DreamRubric.objects.all(), label = "Category", empty_label = None, error_messages={'required': 'Choose category'}, widget=forms.widgets.Select(attrs={'size': 8}))
    #Походу надо всетаки создать модель dreamrubric и связать её 
    
    class Meta:
        model = Biography
        fields = ('bio', 'dream', 'dreamrubric',)
        
        
class EmailForm(forms.ModelForm):
    email = forms.EmailField(label = "", error_messages={'required': 'Enter your Email'})
    
    class Meta:
        model = Email
        fields = ('email',)