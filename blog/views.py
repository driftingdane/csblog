from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .models import Category


def index(request):
	all_posts = Post.newmanager.all()
	all_categories = Category.objects.all()
	page = request.GET.get('page', 1)
	
	paginator = Paginator(all_posts, 3)
	try:
		all_posts = paginator.page(page)
	except PageNotAnInteger:
		all_posts = paginator.page(1)
	except EmptyPage:
		all_posts = paginator.page(paginator.num_pages)
	
	return render(request, 'pages/index.html', {'posts': all_posts, 'categories': all_categories})


def post_single(request, post):
	post = get_object_or_404(Post, slug=post, status='published')
	return render(request, 'pages/single.html', {'post': post})
