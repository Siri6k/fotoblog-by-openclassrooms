
from django.contrib import admin
from django.urls import path

import authentication.views
import  blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #authentification
    path('', authentication.views.login_page, name='login'),
    path('logout/',
         authentication.views.logout_user, name='logout'),
    # Page d'accueil
    path('home/', blog.views.home,
         name='home'),
    #inscription
    path('signup/', authentication.views.signup_page, name='signup'),
]
