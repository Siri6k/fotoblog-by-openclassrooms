from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#restrindre l accès qu aux utilisateur authentifiés
@login_required
def home(request):
    return render(request,
                  'blog/home.html'
                  )