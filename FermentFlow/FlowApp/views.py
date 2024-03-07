from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from FlowApp import forms, models
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

def inicio(request):
    mensaje = "FermentFlow"
    seguimiento_fermentaciones = "Seguimiento de Fermentaciones"
    return render(request, 'FlowApp/inicio.html', {'mensaje': mensaje, 'seguimiento_fermentaciones': seguimiento_fermentaciones})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            login(request, user)            
            return render(request, "FlowApp/inicio.html", {"mensaje": f'Bienvenide {user.username}'})         
    else:
        form = AuthenticationForm()
    return render(request, "FlowApp/login.html", {"form": form})

def register(request):
      if request.method == 'POST':
            form = forms.Form_Registro(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"FlowApp/inicio.html" ,  {"mensaje":"Usuario Creado Exitosamente"})
      else:
            form = forms.Form_Registro()     
      return render(request,"FlowApp/register.html" ,  {"form":form})
  
@login_required

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    models.Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request, "FlowApp/inicio.html")
    else:
        miFormulario = forms.UserEditForm(instance=request.user)
    return render(request, "FlowApp/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'FlowApp/cambiar_clave.html'
    success_url = reverse_lazy('EditarPerfil')

def id_tanques(request):
    if request.method == 'POST':
        formulario = forms.Form_Id_Tanques(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            id_tanque = models.Id_Tanques(id_tanque=informacion["id_tanque"])
            id_tanque.save()
            return render(request, 'FlowApp/inicio.html')
    else:
        formulario = forms.Form_Id_Tanques()
    return render(request, "FlowApp/id_tanques.html", {"formulario": formulario})


class Id_TanquesListView(ListView):
    model = models.Id_Tanques
    context_object_name = "id_tanques"
    template_name = "FlowApp/id_tanques_lista.html"

class Id_TanquesDetailView(DetailView):
    model = models.Id_Tanques
    template_name = "FlowApp/id_tanques_detalle.html" 

class Id_TanquesCreateView(CreateView):
    model = models.Id_Tanques
    template_name = "FlowApp/id_tanque_crear.html"
    success_url = reverse_lazy('ListaIdTanques')
    fields = ['id_tanque']   
    
class Id_TanquesUpdateView(UpdateView):
    model = models.Id_Tanques
    template_name = "FlowApp/id_tanque_editar.html"
    success_url = reverse_lazy('ListaIdTanques')
    fields = ['id_tanque']   

class Id_TanquesDeleteView(DeleteView):
    model = models.Id_Tanques    
    template_name = "FlowApp/id_tanques_borrar.html"
    success_url = reverse_lazy('ListaIdTanques')                                         

def tanques(request):
    if request.method == 'POST':
        formulario = forms.Form_Tanques(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tanque = models.Tanques(
                id_tanque=informacion["id_tanque"],
                fecha=informacion["fecha"],
                variedad=informacion["variedad"],
                t=informacion["t"],
                brix=informacion["brix"],
                ph=informacion["ph"],
                cliente=informacion["cliente"],
                enologo=informacion["enologo"],
                observaciones=informacion.get("observaciones", None)
            )
            tanque.save()
            return render(request, 'FlowApp/tanques.html')
    else:
        formulario = forms.Form_Tanques()
    contexto = {"formulario": formulario}
    return render(request, "FlowApp/tanques.html", contexto)

def mostovino(request):
    if request.method == 'POST':
        formulario = forms.Form_MostoVino(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            mosto_vino = models.MostoVino(variedad=informacion["variedad"])
            mosto_vino.save()
            return render(request, 'FlowApp/mosto_vino.html')
    else:
        formulario = forms.Form_MostoVino()
    contexto = {"formulario": formulario}
    return render(request, "FlowApp/mosto_vino.html", contexto)

def clientes(request):
    if request.method == 'POST':
        formulario = forms.Form_Clientes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cliente = models.Clientes(
                cliente=informacion["cliente"],
                contacto=informacion["contacto"]
            )
            cliente.save()
            return render(request, 'FlowApp/clientes.html')
    else:
        formulario = forms.Form_Clientes()
    contexto = {"formulario": formulario}
    return render(request, "FlowApp/clientes.html", contexto)

def enologos(request):
    if request.method == 'POST':
        formulario = forms.Form_Enologos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            enologo = models.Enologos(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion.get("email", None),
                telefono=informacion["telefono"],
                puesto=informacion["puesto"],
                tipo_contrato=informacion["tipo_contrato"]
            )
            enologo.save()
            return render(request, 'FlowApp/enologos.html')
    else:
        formulario = forms.Form_Enologos()
    contexto = {"formulario": formulario}
    return render(request, "FlowApp/enologos.html", contexto)

