from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='vulnerable'),
    path('vulnerable/<slug:slug_id>/',views.vulnerablechild,name='vulnerablechild')
]
