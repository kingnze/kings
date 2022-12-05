from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('king/', admin.site.urls),
    path('',include('ngo.urls')),
    path('blog',include('blog.urls')),
    path('gallery',include('gallery.urls')),
    path('quote',include('quote.urls')),
    path('objective',include('objective.urls')),
    path('schoolprogram',include('schoolprogram.urls')),
    path('disabled',include('disabled.urls')),
    path('helpthekids',include('helpthekids.urls')),
    path('girlstec',include('girlstec.urls')),
    path('childlove',include('childlove.urls')),
    path('starts',include('starts.urls')),
    path('starts1',include('starts1.urls')),
    path('vulnerable',include('vulnerable.urls')),
    path('fighthunger',include('fighthunger.urls')),
    path('banner',include('banner.urls')),
    path('climatevictims',include('climatevictims.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

