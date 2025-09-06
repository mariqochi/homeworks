


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin # This line is the correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_first_app.urls')),]

if settings.DEBUG:
    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #დამატებულია 29-34
