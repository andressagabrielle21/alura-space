from django import forms

class LoginForms(forms.Form):
  login_username = forms.CharField(label="Nome de login", required=True, max_length=100, widget=forms.TextInput(
    attrs={
      "class": "form-control",
      "placeholder": "Ex: Maria da Silva"
    }
  ))
  password = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(
    attrs={
      "class": "form-control",
      "placeholder": "Digite sua senha"
    }
  ))


class SignupForms(forms.Form):
  signup_username = forms.CharField(label="Nome de cadastro", required=True, max_length=100, widget=forms.TextInput(
    attrs={
      "class": "form-control",
      "placeholder": "Ex: Maria da Silva"
    }
  ))
  email = forms.CharField(label="E-mail", required=True, max_length=100, widget=forms.EmailInput(
    attrs={
      "class": "form-control",
      "placeholder": "Ex: mariasilva@email.com"
    }
  ))
  password = forms.CharField(label="Senha", required=True, max_length=70, widget=forms.PasswordInput(
    attrs={
      "class": "form-control",
      "placeholder": "Digite sua senha"
    }
  ))
  password_check = forms.CharField(label="Confirme sua senha", required=True, max_length=70, widget=forms.PasswordInput(
    attrs={
      "class": "form-control",
      "placeholder": "Confirme sua senha"
    }
  ))