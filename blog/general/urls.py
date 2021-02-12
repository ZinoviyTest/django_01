from django.urls import path
from .views import current_datetime_now


urlpatterns = [
    path('time/', current_datetime_now),
]