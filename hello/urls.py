from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/detail/<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('contact/', contact, name='contact'),
    path('blog/', BlogView.as_view(), name="blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
