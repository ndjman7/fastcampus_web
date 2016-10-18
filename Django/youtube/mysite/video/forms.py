from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = {'kind', 'videoId', 'title', 'description', 'publishedAt', 'thumbnails', }
        widgets = {
            'kind': forms.HiddenInput(),
            'videoId': forms.HiddenInput(),
            'title': forms.HiddenInput(),
            'description': forms.HiddenInput(),
            'publishedAt': forms.HiddenInput(),
            'thumbnails': forms.HiddenInput(),
        }
