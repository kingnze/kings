from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='schoolprogram'),
    path('schoolprogram/<slug:slug_id>/',views.school,name='school')
]