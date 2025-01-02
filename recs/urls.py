from django.urls import path
from .views import RecomendationAPIView

urlpatterns = [
    path('recommendation/', RecomendationAPIView.as_view(), name='recommendation-api'),
]
