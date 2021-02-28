from django.contrib import admin
from django.urls import path 
from cadastro import views


urlpatterns = [  
    path('admin/', admin.site.urls),  
	path('', views.show_menu),  
    path('cadastro-pessoa', views.cadastro_pessoa),  
    path('show-pessoa',views.show_pessoa),  
    path('edit-pessoa/<int:id>', views.edit_pessoa),  
    path('update-pessoa/<int:id>', views.update_pessoa),  
    path('delete-pessoa/<int:id>', views.destroy_pessoa),  
	path('cadastro-sala', views.cadastro_sala),  
    path('show-sala',views.show_sala),  
    path('edit-sala/<int:id>', views.edit_sala),  
    path('update-sala/<int:id>', views.update_sala),  
    path('delete-sala/<int:id>', views.destroy_sala),  
    path('cadastro-espaco', views.cadastro_espaco),  
    path('show-espaco',views.show_espaco),  
    path('edit-espaco/<int:id>', views.edit_espaco),  
    path('update-espaco/<int:id>', views.update_espaco),  
    path('delete-espaco/<int:id>', views.destroy_espaco), 
    path('cadastro-reserva-sala', views.cadastro_reserva_sala),  
    path('show-reserva-sala',views.show_reserva_sala), 
	path('show-reserva-sala-pessoa/<int:id>',views.show_reserva_sala_pessoa), 
    path('edit-reserva-sala/<int:id>', views.edit_reserva_sala),  
    path('update-reserva-sala/<int:id>', views.update_reserva_sala),  
    path('delete-reserva-sala/<int:id>', views.destroy_reserva_sala),
]
