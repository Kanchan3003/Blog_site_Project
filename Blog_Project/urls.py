
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog_app.urls')),
    path('User/', include('django.contrib.auth.urls')),
    path('User/', include('User.urls')),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
