
from django.contrib import admin
from django.urls import path
from django.conf import settings
import authentication.views
import  blog.views

from django.conf.urls.static import static

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
    # Publiez une photo
    path('photo/upload/', blog.views.photo_upload, name="photo_upload"),
    # changer la photo de profil
    path('change/profile/photo/', authentication.views.upload_profile_photo, name="change_profile_photo"),
    #ajouter un billet de blog
    path('blog/create/',
         blog.views.blog_and_photo_upload, name='blog-create'),
    # visualisation d'un bilet de blog
    path('blog/<int:blog_id>/',
         blog.views.view_blog, name="view-blog"),
    # modifier ou supprimer un billet de blog
    path('blog/<int:blog_id>/edit/',
         blog.views.edit_blog, name="edit-blog"),
    # publier multiples photos a la fois
    path('photo/upload-multiple/',
         blog.views.create_multiple_photos,
         name="create-multiple-photos"),
    # relation plusieurs a plusieurs
    path('blog/follow-users/',
         blog.views.follow_users,
         name = "follow-users"),
    # creer un flux avec les photos
    path('blog/photo_feed/',
         blog.views.photo_feed,
         name = "photo-feed"),
]
# ajoutez les medias
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root =settings.MEDIA_ROOT)