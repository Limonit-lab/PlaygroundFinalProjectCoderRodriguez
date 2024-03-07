from django.urls import path
from FlowApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='FlowApp/logout.html', ), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('id_tanques', views.id_tanques, name="Id_Tanques"),
    path('tanques', views.tanques, name="Tanques"),
    path('clientes', views.clientes, name="Clientes"),
    path('enologos', views.enologos, name="Enologos"),
    path('mostovino', views.mostovino, name="MostoVino"),
    path('id_tanques/lista', views.Id_TanquesListView.as_view(), name="ListaId_Tanques"),
    path('id_tanques/nuevo', views.Id_TanquesCreateView.as_view(), name="NuevoId_Tanque"),
    path('id_tanques/<pk>', views.Id_TanquesDetailView.as_view(), name="DetalleId_Tanque"),
    path('id_tanques/<pk>/editar', views.Id_TanquesUpdateView.as_view(), name="EditarId_Tanque"),
    path('id_tanques/<pk>/borrar', views.Id_TanquesDeleteView.as_view(), name="BorrarId_Tanque"),
    
    ]