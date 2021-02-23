from django.shortcuts import render, redirect  

from cadastro.forms import PessoaForm  
from cadastro.models import Pessoa

  
def cadastro_pessoa(request):  
    if request.method == "POST":  
        form = PessoaForm(request.POST) 
 
        if form.is_valid(): 
			# Tratamento de exceção: Não retornar erro na tela  
            try:  
                form.save()  
                return redirect('/cadastro/show-pessoa')  
            except:  
                pass  
    else:  
        form = PessoaForm()  

    return render(request,'index_pessoa.html',{'form':form})


def show_pessoa(request):  
    pessoa = Pessoa.objects.all()  
    return render(request,"show_pessoa.html",{'pessoa': pessoa}) 


def edit_pessoa(request, id):  
    pessoa = Pessoa.objects.get(id_pessoa=id)  
    return render(request,'edit_pessoa.html', {'pessoa': pessoa})  


def update_pessoa(request, id):  
    pessoa = Pessoa.objects.get(id_pessoa=id)  

    form = PessoaForm(request.POST, instance=pessoa)  
    if form.is_valid():  
        form.save()  
        return redirect("/cadastro/show-pessoa")  
    return render(request, 'edit_pessoa.html', {'pessoa': pessoa})  


def destroy_pessoa(request, id):  
    pessoa = Pessoa.objects.get(id_pessoa=id)  
    pessoa.delete()  
    return redirect("/cadastro/show-pessoa")  

