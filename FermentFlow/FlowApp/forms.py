from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class Form_Id_Tanques(forms.Form):
    id_tanque = forms.CharField(max_length=10)

class Form_Tanques(forms.Form):
    id_tanque = forms.CharField(max_length=10)
    fecha = forms.DateField()
    variedad = forms.CharField(max_length=40)
    t = forms.FloatField()
    brix = forms.FloatField()
    ph = forms.FloatField()
    cliente = forms.CharField(max_length=30)
    enologo = forms.CharField(max_length=30)
    observaciones = forms.TextInput()

class Form_MostoVino(forms.Form):
    variedad = forms.CharField(max_length=30)

class Form_Clientes(forms.Form):
    cliente = forms.CharField(max_length=30)
    contacto = forms.EmailField()

class Form_Enologos(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    puesto = forms.CharField(max_length=30)
    tipo_contrato = forms.CharField(max_length=30) 
    
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']

class Form_Registro(UserCreationForm):
    username = forms.TextInput()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)


    