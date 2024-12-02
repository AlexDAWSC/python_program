from django.shortcuts import render, get_object_or_404
from .models import NewsEntry

def news(request):
    # Retrieve the latest 3 news posts, ordered by date
    news = NewsEntry.objects.order_by('-date')[:3]
    
    # Render the news homepage with the latest news posts
    return render(request, 'news/news.html', {'news': news})

def detail(request, news_id):
    # Fetch a specific news post or return a 404 error if not found
    selected_blog_post = get_object_or_404(NewsEntry, pk=news_id)
    
    # Render the detailed view of the selected blog post
    return render(request, 'news/detail.html', {'new': selected_blog_post})