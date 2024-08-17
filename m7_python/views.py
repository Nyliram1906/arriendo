from django.shortcuts import render, redirect
from m7_python.models import *
from m7_python.forms import InmuebleForm, UserForm, TipoForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user=' + str(form.cleaned_data['username']))
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})

def register_tipoView(request):
    username = request.GET['user']
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            user = User.objects.filter(username=username)[0]
            tipo_user = Tipo_user.objects.filter(id=int(tipo))[0]

            # Verificar si el perfil ya existe
            if Profile.objects.filter(user=user).exists():
                profile = Profile.objects.get(user=user)
                profile.id_tipo_user = tipo_user.id
                profile.rut = rut
                profile.direccion = direccion
                profile.telefono = telefono
                profile.save()
            else:
                # Crear un nuevo perfil si no existe
                datos = Profile(user=user, id_tipo_user=tipo_user.id, rut=rut, direccion=direccion, telefono=telefono)
                datos.save()

            return HttpResponseRedirect('/login/')
    else:
        form = TipoForm()

    return render(request, 'registration/register_tipo.html', {'form': form})



@login_required
def dashboardView(request):
    return render(request, 'dashboard.html', {})

def indexView(request):
    return render(request, 'index.html', {})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form}
    return render(request, 'registration/update_profile.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')  # Redirige a una página específica tras el login

@login_required
def new_inmuebleView(request):
    if request.method == 'POST':
        u_form = InmuebleForm(request.POST)
        if u_form.is_valid():
            id_tipo_inmueble = u_form.cleaned_data['id_tipo_inmueble']
            id_comuna = u_form.cleaned_data['id_comuna']
            id_region = u_form.cleaned_data['id_region']
            nombre_inmueble = u_form.cleaned_data['nombre_inmueble']
            descripcion = u_form.cleaned_data['descripcion']
            m2_construido = u_form.cleaned_data['m2_construido']
            numero_banos = u_form.cleaned_data['numero_banos']
            numero_hab = u_form.cleaned_data['numero_hab']
            direccion = u_form.cleaned_data['direccion']
            m2_terreno = u_form.cleaned_data['m2_terreno']
            numero_est = u_form.cleaned_data['numero_est']

            tipo_inmueble = Tipo_inmueble.objects.filter(id=int(id_tipo_inmueble))[0]
            comuna = Comuna.objects.filter(id=int(id_comuna))[0]
            reg = Region.objects.filter(id=int(id_region))[0]
            current_user = request.user

            user = User.objects.filter(id=current_user.id)
            inm = Inmuebles(
                id_tipo_inmueble=tipo_inmueble,
                id_comuna=comuna,
                id_region=reg,
                nombre_inmueble=nombre_inmueble,
                descripcion=descripcion,
                m2_construido=m2_construido,
                numero_banos=numero_banos,
                numero_hab=numero_hab,
                direccion=direccion,
                m2_terreno=m2_terreno,
                numero_est=numero_est
            )
            print(user)
            inm.id_user_id = current_user.id
            inm.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = InmuebleForm()

    context = {'u_form': u_form}
    return render(request, 'new_inmueble.html', context)

 # Aquí puedes agregar la lógica para guardar el inmueble en la base de datos
            # Ejemplo:
            # nuevo_inmueble = Inmueble(
            #     tipo=tipo_inmueble,
            #     comuna=comuna,
            #     region=reg,
            #     nombre=nombre_inmueble,
            #     descripcion=descripcion,
            #     m2_construido=m2_construido,
            #     numero_banos=numero_banos,
            #     numero_hab=numero_hab,
            #     direccion=direccion,
            #     m2_terreno=m2_terreno,
            #     numero_est=numero_est,
            #     usuario=current_user
            # )
            # nuevo_inmueble.save()

            # Redirigir a una página de éxito o mostrar un mensaje de éxito
            # return redirect('success_page')
            
