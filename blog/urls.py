from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='blog'),
    path('blog/<slug:slug_id>/',views.blog,name='blog')
]