from django.shortcuts import render, redirect  

from cadastro.forms import PessoaForm, SalaForm, EspacoForm  
from cadastro.models import Pessoa, Sala, Espaco


# Menu do sistema FIXME TODO
def show_menu(request):  
    return render(request,'index_pessoa.html',{'form':form})


# Cadastro de Pessoa
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


# Cadastro de sala
def cadastro_sala(request):  
    if request.method == "POST":  
        form = SalaForm(request.POST) 
 
        if form.is_valid(): 
			# Tratamento de exceção: Não retornar erro na tela  
            try:  
                form.save()  
                return redirect('/cadastro/show-sala')  
            except:  
                pass  
    else:  
        form = SalaForm()  

    return render(request,'index_sala.html',{'form':form})


def show_sala(request):  
    sala = Sala.objects.all()  
    return render(request,"show_sala.html",{'sala': sala}) 


def edit_sala(request, id):  
    sala = Sala.objects.get(id_sala=id)  
    return render(request,'edit_sala.html', {'sala': sala})  


def update_sala(request, id):  
    sala = Sala.objects.get(id_sala=id)  

    form = SalaForm(request.POST, instance=sala)  
    if form.is_valid():  
        form.save()  
        return redirect("/cadastro/show-sala")  
    return render(request, 'edit_sala.html', {'sala': sala})  


def destroy_sala(request, id):  
    sala = Sala.objects.get(id_sala=id)  
    sala.delete()  
    return redirect("/cadastro/show-sala") 


# cadastro de lotação
def cadastro_espaco(request):  
    if request.method == "POST":  
        form = EspacoForm(request.POST) 
 
        if form.is_valid(): 
			# Tratamento de exceção: Não retornar erro na tela  
            try:  
                form.save()  
                return redirect('/cadastro/show-espaco')  
            except:  
                pass  
    else:  
        form = EspacoForm()  

    return render(request,'index_espaco.html',{'form':form})


def show_espaco(request):  
    espaco = Espaco.objects.all()  
    return render(request,"show_espaco.html",{'espaco': espaco}) 


def edit_espaco(request, id):  
    espaco = Espaco.objects.get(id_espaco=id)  
    return render(request,'edit_espaco.html', {'espaco': espaco})  


def update_espaco(request, id):  
    espaco = Espaco.objects.get(id_espaco=id)  

    form = EspacoForm(request.POST, instance=espaco)  
    if form.is_valid():  
        form.save()  
        return redirect("/cadastro/show-espaco")  
    return render(request, 'edit_espaco.html', {'espaco': espaco})  


def destroy_espaco(request, id):  
    espaco = Espaco.objects.get(id_espaco=id)  
    espaco.delete()  
    return redirect("/cadastro/show-espaco") 



