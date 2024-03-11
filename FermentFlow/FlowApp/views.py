from django.http import HttpResponse
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
    return render(request, "FlowApp/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'FlowApp/cambiarclave.html'
    success_url = reverse_lazy('EditarPerfil')

@login_required

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
    template_name = "FlowApp/id_tanques_crear.html"
    success_url = reverse_lazy('ListaId_Tanques')
    fields = ['id_tanque']   
   
 
class Id_TanquesUpdateView(UpdateView):
    model = models.Id_Tanques
    template_name = "FlowApp/id_tanques_editar.html"
    success_url = reverse_lazy('ListaId_Tanques')
    fields = ['id_tanque']      

class Id_TanquesDeleteView(DeleteView):
    model = models.Id_Tanques    
    template_name = "FlowApp/id_tanques_borrar.html"
    success_url = reverse_lazy('ListaId_Tanques')                                         

@login_required

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

class TanquesListView(ListView):
    model = models.Tanques
    context_object_name = "tanques"
    template_name = "FlowApp/tanques_lista.html"

class TanquesDetailView(DetailView):
    model = models.Tanques
    template_name = "FlowApp/tanques_detalle.html" 

class TanquesCreateView(CreateView):
    model = models.Tanques
    template_name = "FlowApp/tanques_crear.html"
    success_url = reverse_lazy('ListaTanques')
    fields = ["id_tanque","fecha", "variedad", "t", "brix", "ph", "cliente", "enologo", "observaciones"]         
    
class TanquesUpdateView(UpdateView):
    model = models.Tanques
    template_name = "FlowApp/tanques_editar.html"
    success_url = reverse_lazy('ListaTanques')
    fields = ["id_tanque","fecha", "variedad", "t", "brix", "ph", "cliente", "enologo", "observaciones"]   


class TanquesDeleteView(DeleteView):
    model = models.Tanques    
    template_name = "FlowApp/tanques_borrar.html"
    success_url = reverse_lazy('ListaTanques')                                         


def mostovino(request):
    if request.method == 'POST':
        formulario = forms.Form_MostoVino(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            variedad = models.MostoVino(variedad=informacion["variedad"])
            variedad.save()
            return render(request, 'FlowApp/mostovino.html')
    else:
        formulario = forms.Form_MostoVino()
    contexto = {"formulario": formulario}
    return render(request, "FlowApp/mostovino.html", contexto)

class MostoVinoListView(ListView):
    model = models.MostoVino
    context_object_name = "mostovino"
    template_name = "FlowApp/mostovino_lista.html"

class MostoVinoDetailView(DetailView):
    model = models.MostoVino
    template_name = "FlowApp/mostovino_detalle.html" 

class MostoVinoCreateView(CreateView):
    model = models.MostoVino
    template_name = "FlowApp/mostovino_crear.html"
    success_url = reverse_lazy('ListaMostoVino')
    fields = ['variedad']   
    
class MostoVinoUpdateView(UpdateView):
    model = models.MostoVino
    template_name = "FlowApp/mostovino_editar.html"
    success_url = reverse_lazy('ListaMostoVino')
    fields = ['variedad']   

class MostoVinoDeleteView(DeleteView):
    model = models.MostoVino    
    template_name = "FlowApp/mostovino_borrar.html"
    success_url = reverse_lazy('ListaMostoVino')                                         


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

class ClientesListView(ListView):
    model = models.Clientes
    context_object_name = "clientes"
    template_name = "FlowApp/clientes_lista.html"


class ClientesDetailView(DetailView):
    model = models.Clientes
    template_name = "FlowApp/clientes_detalle.html" 



class ClientesCreateView(CreateView):
    model = models.Clientes
    template_name = "FlowApp/clientes_crear.html"
    success_url = reverse_lazy('ListaClientes')
    fields = ['cliente', 'contacto']   
 
    
class ClientesUpdateView(UpdateView):
    model = models.Clientes
    template_name = "FlowApp/clientes_editar.html"
    success_url = reverse_lazy('ListaClientes')
    fields = ['cliente', 'contacto']   


class ClientesDeleteView(DeleteView):
    model = models.Clientes    
    template_name = "FlowApp/clientes_borrar.html"
    success_url = reverse_lazy('ListaClientes')    

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

class EnologosListView(ListView):
    model = models.Enologos
    context_object_name = "enologos"
    template_name = "FlowApp/enologos_lista.html"


class EnologosDetailView(DetailView):
    model = models.Enologos
    template_name = "FlowApp/enologos_detalle.html" 


class EnologosCreateView(CreateView):
    model = models.Enologos
    template_name = "FlowApp/enologos_crear.html"
    success_url = reverse_lazy('ListaEnologos')
    fields = ['nombre', 'apellido', 'email', 'telefono', 'puesto', 'tipo_contrato']  
       
    
class EnologosUpdateView(UpdateView):
    model = models.Enologos
    template_name = "FlowApp/enologos_editar.html"
    success_url = reverse_lazy('ListaEnologos')
    fields = ['nombre', 'apellido', 'email', 'telefono', 'puesto', 'tipo_contrato']  


class EnologosDeleteView(DeleteView):
    model = models.Enologos    
    template_name = "FlowApp/enologos_borrar.html"
    success_url = reverse_lazy('ListaEnologos')


def buscar(request):
    if request.GET['id_tanque']:
        id_tanque = request.GET['id_tanque']
        tanques = models.Tanques.objects.filter(id_tanque__icontains=id_tanque)

        return render(request, 'FlowApp/inicio.html', {'tanques': tanques, 'id_tanque': id_tanque})
    else:
        respuesta = 'No enviaste datos.'
        
    return render(request, 'FlowApp/inicio.html', {'respuesta': respuesta})