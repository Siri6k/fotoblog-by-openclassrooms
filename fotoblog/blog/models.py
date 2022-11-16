from django.db import models
from django.conf import settings
from PIL import Image
class Photo(models.Model):
    image = models.ImageField(verbose_name='Image')
    caption = models.CharField(max_length=128,
                               verbose_name='Légende',
                               blank=True)
    # une photo est post par un user ou uplaoader
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l'image redimensionné
        #dans le systeme de fichiers
        # ce n'est pas la methode save() du modele
        image.save(self.image.path)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Blog(models.Model):
    #une photo sera lié a chaque post si possble
    # SET_NULL -> optionnelle non lié a la photo
    photo = models.ForeignKey(Photo,
                              null=True, on_delete=models.SET_NULL,
                              blank=True)
    title = models.CharField(max_length=128,
                             verbose_name='Titre')
    content = models.CharField(max_length=5000,
                               verbose_name='Contenu')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name='Auteur',
                               on_delete=models.CASCADE,
                               null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)

    word_count = models.IntegerField(verbose_name='Nombre de mots',
                                     null=True)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                          through='BlogContributor',
                                          related_name='contributions')
    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)

class BlogContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255,
                                    blank=True)
    class Meta:
        unique_together = ('contributor', 'blog')