from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)