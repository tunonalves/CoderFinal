from django.shortcuts import render, redirect
from blog.models import Post, Categoria
from .forms import formCat,formPost


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
        forms = formPost(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('Blog')
    else:
        #data['formpost'] = forms
        forms = formPost()
    return render(request,"blog/post.html",{'formpost' : forms})


def formcat(request):
    data = {
        'formcat' : formCat()
    }
    if request.method == 'POST':
        forms = formCat(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Blog')
    else:
        data['formcat'] = forms
    return render(request,"blog/cats.html",data)