from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='disabled'),
    path('disabled/<slug:slug_id>/',views.disabled,name='disabled')
]
