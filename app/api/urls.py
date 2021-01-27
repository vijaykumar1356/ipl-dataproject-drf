from django.urls import path
from app.api.views import (
    problem1_api,
    problem2_api,
    problem3_api,
    problem4_api
)

urlpatterns = [
    path('problem1/', problem1_api),
    path('problem2/', problem2_api),
    path('problem3/', problem3_api),
    path('problem4/', problem4_api),
]
