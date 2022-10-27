from django import forms
from .models import Movie

class Movieform(forms.ModelForm):
    # genre = forms.ChoiceField()

    class Meta:
        model = Movie
        fields = '__all__'
        GENRE_CHOICES = (
            ('', 'Select element'),
            ('코미디', '코미디'),
            ('공포', '공포'),
            ('로맨스', '로맨스'),
        )
        widgets = {
            'genre': forms.Select(choices=GENRE_CHOICES, attrs={'class' : 'form-control'}),
        }

