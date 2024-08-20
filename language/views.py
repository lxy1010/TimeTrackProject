from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, 'language/index.html')

