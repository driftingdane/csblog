from django.shortcuts import render, redirect

from .models import Video


def upload_video(request):
	
	if request.method == 'POST':
		title = request.POST['title']
		video = request.POST['video']
		
		content = Video(title=title, video=video)
		content.save()
		return redirect('home')
	
	return render(request, 'upload.html')


def display(request):
	
	videos = Video.objects.all()
	context = {
		'videos': videos
	}
	
	return render(request, 'videos.html', context)




