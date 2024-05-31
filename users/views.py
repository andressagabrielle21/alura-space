from django.shortcuts import render, redirect
from users.forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(req):
  form = LoginForms()

  if req.method == 'POST':
    form = LoginForms(req.POST)

    if form.is_valid():
      username = form['login_username'].value()
      password = form['password'].value()

      user = auth.authenticate(
        req,
        username=username,
        password=password
      )

      if user is not None:
        auth.login(req, user)
        messages.success(req, f'{username} logado com sucesso!')
        return redirect('index')
      else:
        messages.error(req, 'Erro ao logar. Tente novamente.')
        return redirect('login')

  return render(req, 'users/login.html', {'form': form})
  

def signup(req):
  signup_form = SignupForms()

  if req.method == 'POST':
    form = SignupForms(req.POST)

    if form.is_valid():
      if form["password"].value() != form["password_check"].value():
        messages.error(req, 'As senhas não correspondem.')
        return redirect('signup')
      
      username = form["signup_username"].value()
      email = form["email"].value()
      password = form["password"].value()

      if User.objects.filter(username=username).exists():
        messages.error(req, f'O usuário {username} já existe.')
        return redirect('signup')
      
      user = User.objects.create_user(
        username = username,
        email=email,
        password=password,
      )
      user.save()
      messages.success(req, f'{username} cadastrado com sucesso!')
      return redirect('login')

  return render(req, 'users/signup.html', {'form': signup_form})