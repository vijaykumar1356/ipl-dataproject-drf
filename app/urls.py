from django.urls import path
from app.views import (
    home_view,
    problem1,
    problem2,
    problem3,
    problem4,
)
urlpatterns = [
    path('', home_view, name="home"),
    path('problem1/', problem1),
    path('problem2/', problem2),
    path('problem3/', problem3),
    path('problem4/', problem4),
]
