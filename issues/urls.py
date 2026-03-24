from django.urls import path
from .views import reporters, issues

urlpatterns = [
    path('reporters/', reporters),
    path('issues/', issues),
]
