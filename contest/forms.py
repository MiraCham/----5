from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Contest

class ContestForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'class': 'description-field', 'cols': '22', 'rows': '5'}),
    )
    price = forms.IntegerField(
        label='Цена',
        validators=[
            MinValueValidator(10),
            MaxValueValidator(100),
        ],
        help_text='Рекомендованная розничная цена',
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={'class': 'comment-field', 'cols': '22', 'rows': '5'}),
    )

    class Meta:
        model = Contest
        fields = ['title', 'description', 'price', 'comment']