from django.urls import path
from . import views
app_name ="club"
urlpatterns = [
    path("", views.index, name="index"),
    path("article", views.article, name="article"),
    path("contact", views.contact, name="contact"),
    path("agenda", views.agenda, name="agenda"),
]