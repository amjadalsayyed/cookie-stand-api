from django.urls import path
from .views_front import (
    Cookie_StandCreateView,
    Cookie_StandDeleteView,
    Cookie_StandDetailView,
    Cookie_StandListView,
    Cookie_StandUpdateView,
)

urlpatterns = [
    path("", Cookie_StandListView.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", Cookie_StandDetailView.as_view(), name="cookie_stand_detail"),
    path("create/", Cookie_StandCreateView.as_view(), name="cookie_stand_create"),
    path("<int:pk>/update/", Cookie_StandUpdateView.as_view(), name="cookie_stand_update"),
    path("<int:pk>/delete/", Cookie_StandDeleteView.as_view(), name="cookie_stand_delete"),
]
