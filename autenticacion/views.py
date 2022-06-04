from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class VRegistro(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(selft, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form})

def cerrar_seccion(request):
    logout(request)
    return redirect("Home")

def loguear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("username")
            password_user = form.cleaned_data.get("password")
            user = authenticate(username=name_user,password=password_user)
            if user is not None:
                login(request,user)
                return redirect('Home')
            else:
                messages.error(request, "Usuario No Valido")
        else:
            messages.error(request, "Informacion No Valida")
    form = AuthenticationForm()
    return render(request,"login/login.html",{"form":form})
