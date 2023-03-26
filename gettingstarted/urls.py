from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
from django.urls import path
from django.contrib import auth
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from hello.views.register import RegisterView
from hello.views.comment import CommentCreate
from hello.views.home import home
from hello.views.post import PostView, PostCreate, PostUpdate, PostDelete



app_name = 'hello'

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

# urlpatterns = [
#     path("", hello.views.index, name="index"),
#     path("db/", hello.views.db, name="db"),
#     path("admin/", admin.site.urls),
# ]

urlpatterns = [
    path('hoos/', auth_views.LoginView.as_view(template_name='hello/hoos.html'), name='hoos'),
    path('admin/', admin.site.urls),
    path('login/',
         auth_views.LoginView.as_view(template_name='hello/login.html'),
         name='login'),
    path('ship/', auth_views.LoginView.as_view(template_name='hello/ship.html'), name='ship'),
    path('points/', auth_views.LoginView.as_view(template_name='hello/points.html'), name='points'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hello/hoos.html')),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls'))
]