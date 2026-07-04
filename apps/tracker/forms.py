from django import forms

from .models import ReadingProgress, Review


class ReadingProgressForm(forms.ModelForm):

    class Meta:
        model = ReadingProgress
        fields = [
            "status",
            "current_page",
        ]


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            "rating",
            "text",
        ]