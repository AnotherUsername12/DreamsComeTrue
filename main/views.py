from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User, UserManager

from django.contrib.auth.views import redirect_to_login

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect

from django.urls import reverse

from .forms import BlogForm, SearchForm, BiographyForm, EmailForm, CommentForm

from django.contrib.auth.forms import UserCreationForm


from .models import Blog, Person, Biography, Comment

from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.person.dream != '' or request.user.person.biography != 'Hello. I use ToDo app.':
            request.user.person.stringid = request.user.id
            request.user.save()
            return HttpResponseRedirect(reverse('main:homepage', args=()))
        else:
            request.user.person.stringid = request.user.id
            request.user.save()
            return HttpResponseRedirect(reverse('main:bioedit', args=(request.user.id,)))
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
def homepage(request):
    if request.user.is_authenticated:
        best_category = 0
        best_category_name = 'Отсутствует'
        
        #Сейчас сначала выводятся пользователи любимой категории, а потом уже все остальные. То есть, если у пользователя 0 подписчиков, но он в любимой категории, он будет выводится выше пользователя, у которого больше подписчиков, но не любимая категория.
        #Кстати, циклы в views работают
    
        if best_category < request.user.person.tourism_views:
            best_category = request.user.person.tourism_views
            best_category_name = 'Туризм'
    
        if best_category < request.user.person.travel_views:
            best_category = request.user.person.travel_views
            best_category_name = 'Путешествия'
    
        if best_category < request.user.person.technologies_views:
            best_category = request.user.person.technologies_views
            best_category_name = 'Технологии'
        
        if best_category < request.user.person.car_views:
            best_category = request.user.person.car_views
            best_category_name = 'Автомобили'

        if best_category < request.user.person.food_views:
            best_category = request.user.person.food_views
            best_category_name = 'Еда'

        if best_category < request.user.person.collecting_views:
            best_category = request.user.person.collecting_views
            best_category_name = 'Коллекционирование'

        if best_category < request.user.person.career_views:
            best_category = request.user.person.career_views
            best_category_name = 'Карьера'

        if best_category < request.user.person.health_views:
            best_category = request.user.person.health_views
            best_category_name = 'Здоровье'

        if best_category < request.user.person.meeting_views:
            best_category = request.user.person.meeting_views
            best_category_name = 'Встреча'

        if best_category < request.user.person.other_views:
            best_category = request.user.person.other_views
            best_category_name = 'Другое'
        
        best_person = Person.objects.filter(rubric = best_category_name).order_by('-subscribes')   
        person = Person.objects.exclude(rubric = best_category_name).order_by('-subscribes')
    
        srch = SearchForm(request.POST)
        if srch.is_valid():
            srch = srch.save(commit=False)
            search = srch.search_field
            srch.save()
            return HttpResponseRedirect(reverse('main:search', args=(search,)))
        else:
            context = {'best_person' : best_person, 'person' : person, 'form' : srch}
            return render(request, 'main/index.html', context)

        return render(request, 'main/index.html', {'person' : person,})
    
    else:
        person = Person.objects.order_by('-subscribes')

        return render(request, 'main/index.html', {'person' : person,})

    
def searchinput(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            srch = SearchForm(request.POST)
            if srch.is_valid():
                srch = srch.save(commit=False)
                search = srch.search_field
                srch.save()
                return HttpResponseRedirect(reverse('main:search', args=(search,)))
            else:
                context = {'form' : srch}
                return render(request, 'main/searchinput.html', context)
        else:
            srch = SearchForm(request.POST)
            return render(request, 'main/searchinput.html', {'form' : srch})
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
    
def search(request, search):
    persons = User.objects.filter(username__icontains = search).order_by('id')
    context = {'persons' : persons}
    return render(request, 'main/tasksearch.html', context)
    
def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    comment = Comment.objects.filter(publicationcomment = blog_id)
    comment_id = get_object_or_404(Blog, id = blog_id)
    if str(request.user.id) not in blog.viewers:
        blog.views += 1
        blog.viewers += ' '
        blog.viewers += str(request.user.id)
        blog.save()
        
    if request.method == 'POST':
        cmn = CommentForm(request.POST)
        if cmn.is_valid():
            cmn = cmn.save(commit=False)
            cmn.comment_author = request.user.username
            cmn.publicationcomment = comment_id
            cmn.save()
            return HttpResponseRedirect(reverse('main:detail', args=(blog_id,)))
        else:
            context = {'blog' : blog, 'comment' : comment, 'comment_id' : comment_id, 'form' : cmn}
            return render(request, 'main/detail.html', context)
    else:
        cmn = CommentForm()
        context = {'blog' : blog, 'comment' : comment, 'comment_id' : comment_id, 'form' : cmn}
        return render(request, 'main/detail.html', context)
    
    
def comment_delete(request, blog_id, comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.user.username == comment.comment_author or request.user.is_staff:
        comment.delete()
    return HttpResponseRedirect(reverse('main:detail', args=(blog_id,)))

    
def contact(request, contact_user):
    if request.user.is_authenticated:
        if request.user.person.email != '':
            user = User.objects.get(id = contact_user)
            message = f'Привет, {user.username}! Пользователь {request.user.username} хочет связаться с тобой. Его почта: {request.user.person.email}.'
            send_mail('Dreamer', message, 'morethanicloud@icloud.com', [user.person.email], fail_silently=False)
            return HttpResponseRedirect(reverse('main:profile', args = (contact_user,)))
        else:
            return HttpResponseRedirect(reverse('main:email_edit', args = (request.user.id,)))
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))

def create_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bf = BlogForm(request.POST, request.FILES)
            if bf.is_valid():
                bf = bf.save(commit=False)
                bf.author = request.user.username
                bf.tauthor = Person.objects.get(id = request.user.id)
                bf.authorid = request.user.id
                bf.save()
                return HttpResponseRedirect(reverse('main:profile', args=(request.user.id,)))
            else:
                return render(request, 'main/create.html', {'form' : bf})
        else:
            bf = BlogForm()
            return render(request, 'main/create.html', {'form' : bf})
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))

def delete_blog(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    if request.user.is_authenticated and request.user.username == blog.author:
        blog.image.delete()
        blog.delete()
        return HttpResponseRedirect(reverse('main:profile', args=(blog.authorid,)))
    else:
        return HttpResponseRedirect(reverse('main:detail', args=(blog_id,)))
    
def subscribe_blog(request, author_id):
    if request.user.is_authenticated:
        author = get_object_or_404(User, id = author_id)
        if str(author.id) in request.user.person.subscribed:
            context = {'author' : author}
            return HttpResponseRedirect(reverse('main:profile', args=(author.id,)))
        else:
            author.person.subscribes += 1 
            request.user.person.subscribed += ' '
            request.user.person.subscribed += str(author.id)
            author.person.save()
            request.user.save()
            if author.person.email != '':
                send_mail('TaskControll', 'У вас новый подписчик!', 'morethanicloud@icloud.com', [author.person.email], fail_silently=False)
            context = {'author' : author}
            return HttpResponseRedirect(reverse('main:profile', args=(author.id,)))
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
    
def unsubscribe_blog(request, author_id):
    if request.user.is_authenticated:
        author = get_object_or_404(User, id = author_id)
        if str(author.id) in request.user.person.subscribed:
            author.person.subscribes -= 1 
            request.user.person.subscribed = request.user.person.subscribed.replace(str(author.id), '')
            author.person.save()
            request.user.save()
            context = {'author' : author}
            return HttpResponseRedirect(reverse('main:profile', args=(author.id,)))
        else:
            context = {'author' : author}
            return HttpResponseRedirect(reverse('main:person', args=(author.id,)))
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
def my_subscribes(request):
    if request.user.is_authenticated:
        sub = User.objects.order_by('-id')
        blog = Blog.objects.order_by('-published')
        context = {'sub' : sub, 'blog' : blog}
        return render(request, 'main/my_subscribes.html', context)
    else: 
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
def profile(request, aid):
    if request.user.is_authenticated:
        blog = Blog.objects.order_by('-published')
        profileauthor = User.objects.get(id = aid)
    
        if request.user.id != profileauthor.id:
            if profileauthor.person.rubric == 'Путешествия' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.travel_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
        
            if profileauthor.person.rubric == 'Другое' and str(profileauthor.id) not in                 request.user.person.visited_profile:
                request.user.person.other_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Технологии' and str(profileauthor.id) not in             request.user.person.visited_profile:
                request.user.person.technologies_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Автомобили' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.car_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Здоровье' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.health_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Карьера' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.career_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Встреча' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.meeting_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Еда' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.food_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
            if profileauthor.person.rubric == 'Туризм' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.tourism_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
        
            if profileauthor.person.rubric == 'Коллекционирование' and str(profileauthor.id) not in request.user.person.visited_profile:
                request.user.person.collecting_views += 1
                request.user.person.visited_profile += ' '
                request.user.person.visited_profile += str(profileauthor.id)
                request.user.person.save()
    
        context = {'blog' : blog, 'aid' : aid, 'profileauthor' : profileauthor}
        return render(request, 'main/profile.html', context)
    else: 
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
#Чтобы сделать сортировку профилей по просматриваемым категориям пользователя, сделать поле rubric у person с выбором queryset в forms из десяти уже созданных категорий. Дальше добавить по полю-счётчику просмотров с каждой категории. Например, travelviewscounter, которому в результате просмотра профиля с категорией travel добавляется просмотр. Далее, сделать в контроллере index распределение категорий по более просматриваемым, как best_category и так далее.
def biography_edit(request, aid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pbi = get_object_or_404(User, id = aid)
            bf = BiographyForm(request.POST)
            if bf.is_valid():
                bf = bf.save(commit=False)
                pbi.person.biography = bf.bio
                pbi.person.dream = bf.dream
                pbi.person.rubric = bf.dreamrubric
                bf.save()
                pbi.save()
                request.user.save()
                return HttpResponseRedirect(reverse('main:profile', args=(pbi.id,)))
            else:
                return render(request, 'main/biography_edit.html', {'form' : bf})
        else:
            bf = BiographyForm()
            return render(request, 'main/biography_edit.html', {'form' : bf})
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
def email_edit(request, aid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pem = get_object_or_404(User, id = aid)
            ef = EmailForm(request.POST)
            if ef.is_valid():
                ef = ef.save(commit=False)
                pem.person.email = ef.email
                ef.save()
                pem.save()
                request.user.save()
                send_mail('Dreamer', 'Здравствуйте, это письмо от веб-сайта Dreamer. Вы успешно привязали свою почту!', 'morethanicloud@icloud.com', [pem.person.email], fail_silently=False)
                return HttpResponseRedirect(reverse('main:profile', args=(pem.id,)))
            else:
                return render(request, 'main/email_edit.html', {'form' : ef})
        else:
            ef = EmailForm()
            return render(request, 'main/email_edit.html', {'form' : ef})
    else:
        return HttpResponseRedirect(reverse('main:login', args = ()))
    
def registerview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index', args=()))
    else:
        form = UserCreationForm()
        
    return render(request, 'main/register.html', {'form' : form})