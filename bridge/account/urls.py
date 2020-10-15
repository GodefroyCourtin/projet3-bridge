from django.urls import path
from . import views

app_name ="account"

urlpatterns = [
    path("my_account", views.my_account, name="my_account"),
    path(
        "inscription_producteur",
        views.inscription_producteur,
        name="inscription_producteur",
    ),
    path("connexion", views.connexion, name="connexion"),
]