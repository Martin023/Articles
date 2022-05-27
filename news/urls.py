from importlib.resources import read_binary
# to add the serving upoaded images code we neet these 2 following importations.
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path


from . import views

urlpatterns = [
    
    path('', views.news_today, name='newsToday'),
    re_path('about/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    
    path('search/' ,views.search_results,name='search_results'),
    re_path(r'^article/(\d+)',views.article,name ='article'),
    #We create an article route and we capture an integer which will be the id of the article. 
]
# To serve uploaded images on the development server we need to 
# configure our urls.py to register the MEDIA_ROOT route.


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)