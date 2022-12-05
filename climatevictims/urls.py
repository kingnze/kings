from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='climatevitims'),
    path('climatevitims/<slug:slug_id>/',views.climate,name='climate')
]
