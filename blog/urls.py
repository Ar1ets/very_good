from django.urls import path
from blog import views, vote, search
urlpatterns = [
    path('', views.index),
    path('vote.py', vote.main),
    path('search.py', search.main)
]