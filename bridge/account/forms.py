from django import forms


class Signup(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
        ),
    )
    last_name = forms.CharField(
        label="Nom",
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Prénom"}
        ),
    )
    first_name = forms.CharField(
        label="Prénom",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "E-mail"}
        ),
    )
    password = forms.CharField(
        label="Mot de passe",
        min_length=8,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Mot de passe"}
        ),
    )


class Signin(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
        ),
    )
    password = forms.CharField(
        label="Mot de passe",
        min_length=8,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Mot de passe"}
        ),
    )