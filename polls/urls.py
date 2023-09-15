from django.urls import path
from .views import GetStreet,CreateStreet,GetCreateStreet,DetailUpdateDestroy



urlpatterns = [
    path('getStreet/',GetStreet.as_view()),
    path('createStreet/',CreateStreet.as_view()),
    path('getcreateStreet/',GetCreateStreet.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]