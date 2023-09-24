from django.urls import path
from .views import Notes, NoteDetail , SubscribeView
from . import views
urlpatterns = [
    path('apiview', Notes.as_view()),
    path('', Notes.as_view()),
    path('<str:pk>', NoteDetail.as_view()),
    path('test', views.test, name="test"),
    path('run-test', views.test_second_function, name="test_second_function"),
    path("subscribe", SubscribeView.as_view(), name="subscribe-newsletter")
]

