from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='helpthekids'),
    path('helpthekids/<slug:slug_id>/',views.sustainschool,name='sustainschool')
]