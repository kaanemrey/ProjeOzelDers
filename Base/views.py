from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm



def login_page(request):
  sayfa = 'login'
  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'Böyle bi kullanıcı ismi bulunmuyor')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('Home')
    else:
      messages.error(request, 'Yanlış Şifre')
  context = {'sayfa': sayfa}
  return render(request, 'Log-Sign.html',context)

def logout_user(request):
  logout(request)
  return redirect('Home')

def register_page(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      login(request,user)
      return redirect('Home')
    else:
      messages.error(request,'Kayıt Sırasında Bir Hata Oluştu')
  return render(request, 'Log-Sign.html', {'form' : form })



def MainPage(request):
  return render(request,'MainPage.html')

