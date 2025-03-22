from django.urls import path
from core import views

urlpatterns = [
    path("profile/", views.ProfileList.as_view(), name="person-list"),
    path("profile/<int:pk>/", views.ProfileDetail.as_view(), name="person-detail"),
]