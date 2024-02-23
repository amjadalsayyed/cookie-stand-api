from django.urls import path
from .views import Cookie_StandList, Cookie_StandDetail

urlpatterns = [
    path("", Cookie_StandList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", Cookie_StandDetail.as_view(), name="cookie_stand_detail"),
]
