from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='girlstec'),
    path('girlstec/<slug:slug_id>/',views.girlstec,name='girlstec')
    
]