from django.urls import path
from FlowApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='FlowApp/logout.html', ), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('cambiarclave', views.CambiarClave.as_view(), name="CambiarClave"),
    path('id_tanques', views.id_tanques, name="Id_Tanques"),
    path('tanques', views.tanques, name="Tanques"),
    path('clientes', views.clientes, name="Clientes"),
    path('enologos', views.enologos, name="Enologos"),
    path('mostovino', views.mostovino, name="MostoVino"),
    path('id_tanques/lista', views.Id_TanquesListView.as_view(), name="ListaId_Tanques"),
    path('id_tanques/nuevo', views.Id_TanquesCreateView.as_view(), name="NuevoId_Tanques"),
    path('id_tanques/<int:pk>', views.Id_TanquesDetailView.as_view(), name="DetalleId_Tanques"),
    path('id_tanques/<int:pk>/editar', views.Id_TanquesUpdateView.as_view(), name="EditarId_Tanques"),
    path('id_tanques/<int:pk>/borrar', views.Id_TanquesDeleteView.as_view(), name="BorrarId_Tanques"),
    path('tanques/lista', views.TanquesListView.as_view(), name="ListaTanques"),
    path('tanques/int:<pk>', views.TanquesDetailView.as_view(), name="DetalleTanques"),
    path('tanques/nuevo', views.TanquesCreateView.as_view(), name="NuevoTanque"),
    path('tanques/<int:pk>/editar', views.TanquesUpdateView.as_view(), name="EditarTanques"),
    path('tanques/<int:pk>/borrar', views.TanquesDeleteView.as_view(), name="BorrarTanques"),
    path('mostovino/lista', views.MostoVinoListView.as_view(), name="ListaMostoVino"),
    path('mostovino/nuevo', views.MostoVinoCreateView.as_view(), name="NuevoMostoVino"),
    path('mostovino/<pk>', views.MostoVinoDetailView.as_view(), name="DetalleMostoVino"),
    path('mostovino/<pk>/editar', views.MostoVinoUpdateView.as_view(), name="EditarMostoVino"),
    path('mostovino/<pk>/borrar', views.MostoVinoDeleteView.as_view(), name="BorrarMostoVino"),
    path('clientes/lista', views.ClientesListView.as_view(), name="ListaClientes"),
    path('clientes/nuevo', views.ClientesCreateView.as_view(), name="NuevoClientes"),
    path('clientes/<pk>', views.ClientesDetailView.as_view(), name="DetalleClientes"),
    path('clientes/<pk>/editar', views.ClientesUpdateView.as_view(), name="EditarClientes"),
    path('clientes/<pk>/borrar', views.ClientesDeleteView.as_view(), name="BorrarClientes"),
    path('enologos/lista', views.EnologosListView.as_view(), name="ListaEnologos"),
    path('enologos/nuevo', views.EnologosCreateView.as_view(), name="NuevoEnologos"),
    path('enologos/<int:pk>', views.EnologosDetailView.as_view(), name="DetalleEnologos"),
    path('enologos/<int:pk>/editar', views.EnologosUpdateView.as_view(), name="EditarEnologos"),
    path('enologos/<int:pk>/borrar', views.EnologosDeleteView.as_view(), name="BorrarEnologos"),
    
    ]

