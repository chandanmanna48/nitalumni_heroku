from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
   
    path('gallery',views.gallery,name='gallery'),
    path('highlight',views.highlight,name='highlight_viewall'),
    path('news',views.news,name='news_viewall'),
    path('announcement',views.announcement,name='announcement_viewall'),
]