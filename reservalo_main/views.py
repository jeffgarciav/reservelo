from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Bicicleta,Orden
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm as ccf
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    lista_articulos = Bicicleta.objects.all()
    context ={
        'lista_articulos':lista_articulos,
    }
    return render(request,'reservalo_main/index.html', context)

def articulos(request,bicicleta_id):
    bicicleta = Bicicleta.objects.get(pk=bicicleta_id)
    context ={
        'bicicleta':bicicleta,
    }
    return render(request,'reservalo_main/articulo.html', context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # If authentication is successful, log the user in
                login(request, user)
                return redirect('index')  # Redirect to a home page or dashboard
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'reservalo_main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = ccf(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Bienvenido {username}, la cuenta fue creada con exito')
            return redirect('index')
    else:
        form = ccf()
    return render(request,'reservalo_main/registro.html',{'form':form})

@login_required
def user_profile(request):
    return render(request, 'reservalo_main/perfil.html')

def checkout(request):
    
    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")

        order = Orden(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode)
        order.save()


    return render(request,'reservalo_main/checkout.html')