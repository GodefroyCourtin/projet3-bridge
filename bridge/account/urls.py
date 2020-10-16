from django.urls import path
from . import views

app_name ="account"

urlpatterns = [
    path("my_account", views.my_account, name="my_account"),
    path(
        "inscription",
        views.inscription,
        name="inscription",
    ),
    path("connexion", views.connexion, name="connexion"),
    path("deconnexion", views.deconnexion, name="deconnexion"),
]