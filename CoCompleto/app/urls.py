from django.urls import path
from .views import index, about, ayuda, contact, gallery, product, quienes_somos, service,registro,login

urlpatterns = [
    path('', index, name= "index"),
    path('index/', index, name= "index"),
    path('about/', about, name= "about"),
    path('ayuda/', ayuda, name= "ayuda"),
    path('contact/', contact, name= "contact"),
    path('gallery/', gallery, name= "gallery"),
    path('product/', product, name= "product"),
    path('quienes_somos/', quienes_somos, name= "quienes_somos"),
    path('service/', service, name= "service"),
    path('login/', login, name= "login"),
    path('registro/', registro, name= "registro"),
]