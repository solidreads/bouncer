# Create your views here.
from django.shortcuts import render


def landing(request):

    """Render the landing page."""
    return render(request, 'bouncer/index.html')
