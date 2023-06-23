from django.shortcuts import render
from .forms import ContactoFrom

# Create your views here.
def index (request):
    return render(request,'app/index.html')

def about (request):
    return render(request,'app/about.html')

def ayuda (request):
    return render(request,'app/ayuda.html')

def contact (request):
    data = {
        'form': ContactoFrom()
    }
    if request.method == 'POST':
        formulario = ContactoFrom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto guardado"
        else:
            data["form"]=formulario
            
    return render(request,'app/contact.html', data)

def gallery (request):
    return render(request,'app/gallery.html')

def product (request):
    return render(request,'app/product.html')

def quienes_somos (request):
    return render(request,'app/quienes somos.html')

def service (request):
    return render(request,'app/service.html')

def login (request):
    return render(request,'app/login.html')

def registro (request):
    return render(request,'app/registro.html')