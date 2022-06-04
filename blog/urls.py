from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('',views.blog, name="Blog"),
    path('post/',views.formpost,name="post"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
]