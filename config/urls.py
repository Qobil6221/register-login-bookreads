from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from config import settings
from django.conf.urls.static import static

from config.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('user/', include("users.urls")),
    path('books/', include("users.books")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
