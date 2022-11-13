from django.db import models
from django.conf import settings

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128,
                               blank=True)
    # une photo est post par un user ou uplaoader
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    #une photo sera lié a chaque post si possble
    # SET_NULL -> optionnelle non lié a la photo
    photo = models.ForeignKey(Photo,
                              null=True, on_delete=models.SET_NULL,
                              blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
