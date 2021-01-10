from django.contrib import admin
from django.urls import path

from .views import homepage, index, blog_detail, create_blog, delete_blog, searchinput, by_category, search, registerview, subscribe_blog, unsubscribe_blog, my_subscribes, profile, biography_edit, email_edit, contact, comment_delete

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('homepage/', homepage, name='homepage'),
    path('by_category/<str:category>', by_category, name='by_category'),
    path('email/<str:aid>/', email_edit, name = 'email_edit'),
    path('contact/<str:contact_user>/', contact, name = 'contact'),
    path('biography_edit/<str:aid>/', biography_edit, name = 'bioedit'),
    path('profile/<str:aid>/', profile, name = 'profile'),
    path('detail/<str:blog_id>/<str:comment_id>', comment_delete, name = 'comment_delete'),
    path('detail/<int:author_id>/subscribe/', subscribe_blog, name = 'subscribe'),
    path('detail/<int:author_id>/unsubscribe/', unsubscribe_blog, name = 'unsubscribe'),
    path('my_subscribes/', my_subscribes, name='my_subscribes'),
    path('register/', registerview, name = 'register'),
    path('add/', create_blog, name = 'add'),
    path('delete/<int:blog_id>/', delete_blog, name = 'delete'),
    path('searchuser/', searchinput, name = 'searchinput'),
    path('search/<str:search>/', search, name = 'search'),
    path('detail/<int:blog_id>/', blog_detail, name = 'detail'),
    path('accounts/login/', LoginView.as_view(redirect_field_name='main:add', template_name="main/login_website.html"), name = 'login'),
    path('accounts/logout/', LogoutView.as_view(next_page='main:homepage', template_name = "logged_out_website.html"), name = 'logout'),
]