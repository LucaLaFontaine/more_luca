from django import forms

from .models import Card, Carousel, Photo

INPUT_CLASSES = 'w-full py-4 px-6 rouded-xl border'

class NewCarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title', 'description', ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            # 'Photo': forms.FileInput(attrs={
            #     'class': INPUT_CLASSES,
            #     'multiple': True,
            # }),
        }

class NewPhotosForm(NewCarouselForm):
    photos = forms.FileField(widget=forms.ClearableFileInput(
        attrs={
            'class': INPUT_CLASSES,
            'multiple': True}
    ))
    class Meta(NewCarouselForm.Meta):
        fields = NewCarouselForm.Meta.fields + ['photos',]

