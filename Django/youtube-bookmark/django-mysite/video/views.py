from django.shortcuts import render ,get_object_or_404
from .forms import VideoForm , CategoryForm
from django.shortcuts import redirect
from .models import Video, VideoCategory


def index(request):
    videocategories = VideoCategory.objects.all()
    return render(request, 'category_list.html', {'videocategories': videocategories})


def category_video_list(request, pk):
    videocategory = get_object_or_404(VideoCategory, pk=pk)
    videos = videocategory.video_set.all()
    return render(request, 'category_video_list.html', {'videocategory': videocategory, 'videos': videos})


def category_edit(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('video:category_detail', pk=category.pk)
    else:
        form = CategoryForm()
        return render(request, 'category_edit.html', {'form': form})


def video_list(request, pk, pk2):
    videocategory = get_object_or_404(VideoCategory, pk=pk)
    video =videocategory.video_set.get(pk=pk)
    return render(request, 'video_list.html', {'video': video})

def video_new(request):
    pass
