from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('new', views.create_cliente, name='create_cliente'),
    path('update/<int:id>', views.update_cliente, name='update_cliente'),
    path('delete/<int:id>', views.delete_cliente, name='delete_cliente'),
]
