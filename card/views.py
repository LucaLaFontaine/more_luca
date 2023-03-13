from django.shortcuts import render

# Create your views here.
from card.models import Card, Carousel

def home(request):
    cards = Carousel.objects.all()

    return render(request, 'pages/home.html', {
        'cards': cards,
        # 'carousels': Carousel,
    })
