from django.test import TestCase
from FlowApp.models import Clientes
from django.urls import reverse
from django.contrib.auth import get_user_model

class VerificarRutas(TestCase):
    def test_pagina_inicio(self):
        url = reverse('Inicio')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        
class EliminarClientesTest(TestCase):
    def setUp(self):
        self.cliente = Clientes.objects.create(cliente="Libertad", contacto="libertad@libertad.com")
        user = get_user_model()
        user.objects.create_user('username', password="genericpassword123454321")
    
    def test_setup(self):
        """
        Verificar que creo adecuadamente la instancia de estudiante
        """
        self.assertQuerysetEqual(Clientes.objects.filter(cliente__icontains="Libertad", contacto__icontains="libertad@libertad.com").values(), 
                                 [{ 'contacto': 'libertad@libertad.com', 'id': 1, 'cliente': 'Libertad'}])
    
    def test_login(self):
        """
        Verificar que se inicie sesión
        """
        self.assertTrue(self.client.login(username='username', password='genericpassword123454321'))
    

    def test_eliminar_clientes(self):
        """
        Verificar que se elimine estudiante al iniciar sesión
        """
        self.client.login(username='username', password='genericpassword123454321')
        url = reverse('Borrar_Clientes', args=[self.estudiante.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Clientes.objects.filter(cliente__icontains="Libertad", contacto__icontains="libertad@libertad.com"), 
                                 [])

    def test_no_eliminar_clientes(self):
        """
        Verificar que NO se elimine estudiante sin iniciar sesión
        """
        url = reverse('Borrar_Clientes', args=[self.cliente.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Clientes.objects.filter(cliente__icontains="Libertad", contacto__icontains="libertad@libertad.com").values(), 
                                 [{ 'contacto': 'libertad@libertad.com', 'id': 1, 'cliente': 'Libertad'}])