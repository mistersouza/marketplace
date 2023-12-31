from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', include('item.urls')),
    path('item/', views.item, name='item'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
