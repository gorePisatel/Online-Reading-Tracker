from django import forms
from django.core.exceptions import ValidationError

from .models import ReadingProgress, Review


class ReadingProgressForm(forms.ModelForm):

    class Meta:
        model = ReadingProgress
        fields = ['status', 'current_page',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        book = self.instance.book if self.instance and self.instance.pk else None

        if book:
            self.fields['current_page'].widget.attrs.update({
                'min': 0,
                'max': book.total_pages,
            })

    def clean_current_page(self):
        current_page = self.cleaned_data['current_page']
        book = self.instance.book if self.instance and self.instance.pk else None

        if book and current_page > book.total_pages:
            raise ValidationError('Current page cannot be greater than total pages.')

        return current_page


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'text',]
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'text': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 1 or rating > 5:
            raise ValidationError('Rating must be between 1 and 5.')

        return rating
