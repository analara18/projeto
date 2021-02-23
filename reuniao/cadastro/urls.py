from django.contrib import admin
from django.urls import path 
from cadastro import views


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('cadastro-pessoa', views.cadastro_pessoa),  
    path('show-pessoa',views.show_pessoa),  
    path('edit-pessoa/<int:id>', views.edit_pessoa),  
    path('update-pessoa/<int:id>', views.update_pessoa),  
    path('delete-pessoa/<int:id>', views.destroy_pessoa),  
]  
