from django.urls import path
from .views import Gaims

urlpatterns = [
    path('articles/', Gaims.as_view(), name='articles-gaims'),
]