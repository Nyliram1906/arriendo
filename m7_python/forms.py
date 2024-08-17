from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Comuna, Region, Tipo_user


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    first_name.label = 'Nombre'
    last_name = forms.CharField()
    last_name.label = 'Apellido'
    email = forms.EmailField()
    email.label = 'Correo Electrónico'
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            'username': _('Nombre de Usuario')
        }

class TipoForm(forms.Form):
    tipos = (('1', 'Arrendatario'), ('2', 'Arrendador'),)
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='rut', max_length=100)
    direccion = forms.CharField(label='direccion', max_length=100)
    telefono = forms.CharField(label='telefono', max_length=100)

class UserUpdateForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("El apellido solo debe contener letras.")
        return last_name   
        

class InmuebleForm(forms.Form):
    tipos = (
        (1, "Casa"),
        (2, "Departamento"),
        (3, "Parcela"),
        (4, "Estacionamiento"),
        (5, "Otro")
    )
    id_tipo_inmueble = forms.ChoiceField(choices=tipos)

    comunas = [(x.id, x.comuna) for x in list(Comuna.objects.all())]

    def nombre_comuna(e):
        return e[1]

    comunas.sort(key=nombre_comuna)
    id_comuna = forms.ChoiceField(choices=comunas)

    regiones = [(x.id, x.region) for x in list(Region.objects.all())]
    id_region = forms.ChoiceField(choices=regiones)

    nombre_inmueble = forms.CharField(label='Nombre Inmueble', max_length=100)
    descripcion = forms.CharField(label='Descripción del Inmueble', max_length=100)
    m2_construido = forms.CharField(label='M2 construidos', max_length=100)
    numero_banos = forms.CharField(label='Número de Baños', max_length=100)
    numero_hab = forms.CharField(label='Número de habitaciones', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=100)
    m2_terreno = forms.CharField(label='M2 de terreno', max_length=100)
    numero_est = forms.CharField(label='Número de Estacionamientos', max_length=100)

""" from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("El apellido solo debe contener letras.")
        return last_name
 """