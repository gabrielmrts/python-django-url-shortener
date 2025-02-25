from django.urls import path
from .views import URLShortenerView, RedirectView

urlpatterns = [
    path('urls/', URLShortenerView.as_view(), name='url-shortener'),
    path('urls/<str:short_code>', RedirectView.as_view(), name='redirect-url'),
]