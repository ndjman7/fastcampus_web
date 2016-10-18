from django import forms
from .models import Video , VideoCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = VideoCategory
        fields = ('category_name', )


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('category', 'ubloader', 'title', 'address', 'view_count', 'like_count', )