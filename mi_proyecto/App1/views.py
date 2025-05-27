from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ContactForm

# Create your views here.
def index (request):
    return render(request, 'index.html')

def clientes (request):
    cliente = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': cliente})

def contacto(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': ContactForm})
    