from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = (
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.random, name="random"),
    path("<str:entry>", views.entry, name="entry"),
    path("<str:entry>/edit", views.edit, name="edit")


)
