from django.shortcuts import render
from blog.models import Post, Categoria
from .forms import formCat,formPost
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def blog(request):

    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria,"posts": posts })



def formpost(request):
    data = {
        'formpost' : formPost()
    }
    if request.method == 'POST':
        forms = formPost(data=request.POST)
        if forms.is_valid():
            forms.save()
        else:
            data['formpost'] = forms
    return render(request,"blog/post.html",data)



def formcat(request):
    data = {
        'formcat' : formCat()
    }
    if request.method == 'POST':
        forms = formCat(data=request.POST)
        if forms.is_valid():
            forms.save()
        else:
            data['formcat'] = forms
    return render(request,"blog/cats.html",data)