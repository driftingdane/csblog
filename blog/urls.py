from django.urls import path, re_path, include
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('articles/<slug:post>/', views.post_single, name='post_single'),

]
