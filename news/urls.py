from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # Homepage of the news, displaying a list of posts
    path('', views.news, name='news'),
    
    # Detail view for a specific blog post based on its ID
    path('<int:news_id>/', views.detail, name='detail'),
]
