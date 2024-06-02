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

  def clean_signup_username(self):
    name = self.cleaned_data.get('signup_username')

    if name:
      name = name.strip()
      if ' ' in name:
        raise forms.ValidationError('Espaços não são permitidos no campo de Nome de Cadastro')
      else:
        return name
      
  def clean_password_check(self):
    password = self.cleaned_data.get("password")
    password_check = self.cleaned_data.get("password_check")

    if password and password_check:
      if password != password_check:
        raise forms.ValidationError("As senhas não correspondem.")
      else:
        return password_check