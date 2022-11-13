from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
# Create your views here.
#restreinndre l accès qu aux utilisateur authentifiés
@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request,
                  'blog/home.html',
                  context={'photos':photos})
@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST,
                               request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving model
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    return render(request,
                  'blog/photo_upload.html',
                  context = {'form': form})

@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm
    photo_form = forms.PhotoForm
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST,
                                     request.FILES)
        if all([blog_form.is_valid(),
                photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')

    context = {
        'blog_form': blog_form,
        'photo_form': photo_form
    }
    return render(request,
                  'blog/create_blog_post.html',
                  context=context)