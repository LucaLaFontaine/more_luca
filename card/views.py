from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from card.models import Card, Carousel, ImageSet, Photo
from .forms import NewPhotosForm

def home(request):
    cards = Carousel.objects.all()

    return render(request, 'pages/home.html', {
        'cards': cards,
        # 'carousels': Carousel,
    })

@login_required
def newPost(request):
    if request.method == 'POST':
        form = NewPhotosForm(request.POST, request.FILES)
        photos = request.FILES.getlist('photos')
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            if photos:
                for photo in photos:
                    Photo.objects.create(imageSet=post, image=photo)

            return redirect('home')

    form = NewPhotosForm()

    return render(request, 'card/form.html', {
        'form': form,
        'title': 'New Carousel',
    })
