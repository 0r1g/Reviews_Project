from django.shortcuts import render
from .models import Review

# Create your views here.


def show_reviews(request):
    return render(request, 'reviews/index.html', {'reviews': Review.objects.all()})
