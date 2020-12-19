from django.urls import path
from .views import LiveNewsView
app_name = "news-generation"
urlpatterns = [
    path('live-news/', LiveNewsView.as_view()),
]