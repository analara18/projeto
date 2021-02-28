from django.shortcuts import render, redirect

from cadastro.forms import PessoaForm, SalaForm, EspacoForm, ReservaSalaForm, ReservaSalaPessoaForm  
from cadastro.models import Pessoa, Sala, Espaco, ReservaSala, ReservaSalaPessoa, ReservaSalaPessoa


# Menu do sistema FIXME TODO
def show_menu(request):  
    return render(request,'index.html')


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


# cadastro de Reserva - Sala
def cadastro_reserva_sala(request):  
	if request.method == "POST":
		form = ReservaSalaForm(request.POST) 
 
		if form.is_valid(): 
			# Tratamento de exceção: Não retornar erro na tela  
			try:
				
				sala = Sala.objects.filter(id_sala=request.POST['id_sala'])
				lotacao = list(sala.values())[0]['lotacao']
				
				if len(request.POST.getlist('pessoa')) > lotacao:
					return render(request,'show_sala_erro.html')

				turma = form.save() 

				for pessoa in request.POST.getlist('pessoa'):
					form_turma = {
						'id_reserva': turma.id_reserva,
						'pessoa_id': pessoa
					}
					
					form_reserva = ReservaSalaPessoaForm(form_turma)
					if form_reserva.is_valid():
						form_reserva.save()
				 
				return redirect('/cadastro/show-reserva-sala')
			except:  
				pass  
	else:
		form = ReservaSalaForm()  
		pessoas = Pessoa.objects.all()

	return render(request,'index_reserva_sala.html',{'form':form, 'pessoas': pessoas})


def show_reserva_sala(request):  
    reserva = ReservaSala.objects.all()  
    return render(request,"show_reserva_sala.html",{'reserva': reserva}) 


def show_reserva_sala_pessoa(request, id):
	data_list = []

	reserva = ReservaSala.objects.get(id_reserva=id)
	reserva_list = list(ReservaSalaPessoa.objects.filter(id_reserva=id).values())

	for reserva_dict in reserva_list:		
		pessoa = list(Pessoa.objects.filter(id_pessoa=reserva_dict['pessoa_id_id']).values())[0]
		pessoa_str = "%s %s" % (pessoa['nome'], pessoa['sobrenome'])
		data_list.append(pessoa_str)
	
	return render(request,"show_reserva_sala_pessoa.html",{'reserva': reserva.nome, 'pessoas': data_list}) 


def edit_reserva_sala(request, id):  
	reserva = ReservaSala.objects.get(id_reserva=id)  
	pessoas = Pessoa.objects.all()
	
	pessoa_list = []
	for pessoa in list(pessoas.values()):
		pessoa_dict = {
			'id_pessoa': pessoa['id_pessoa'],
			'nome': pessoa['nome'],
		}

		reservado = ReservaSalaPessoa.objects.filter(pessoa_id=pessoa['id_pessoa']).filter(id_reserva=id)
		if reservado:
			pessoa_dict['checked'] = True
		else:
			pessoa_dict['checked'] = False
		pessoa_list.append(pessoa_dict)

	return render(request,'edit_reserva_sala.html', {'reserva': reserva, 'pessoas': pessoa_list})  


def update_reserva_sala(request, id):  
	reserva = ReservaSala.objects.get(id_reserva=id)
	if reserva:
		try:				
			if len(request.POST.getlist('pessoa')) > reserva.id_sala.lotacao:
				return render(request,'show_sala_erro.html')

			ReservaSala.objects.filter(id_reserva=id).update(nome=request.POST['nome'])

			for reserva_dict in list(ReservaSalaPessoa.objects.filter(id_reserva=id).values()):
				reserva = ReservaSalaPessoa.objects.get(id_reserva_pessoa=reserva_dict['id_reserva_pessoa']) 
				reserva.delete()

			for pessoa in request.POST.getlist('pessoa'):
				form_turma = {
					'id_reserva': id,
					'pessoa_id': pessoa
				}
					
				form_reserva = ReservaSalaPessoaForm(form_turma)
				if form_reserva.is_valid():
					form_reserva.save()
				
			return redirect("/cadastro/show-reserva-sala")
		except:
			pass

	return render(request, 'edit_reserva_sala.html', {'reserva': reserva})  


def destroy_reserva_sala(request, id):  
    reserva = ReservaSala.objects.get(id_reserva=id)  
    reserva.delete()  
    return redirect("/cadastro/show-reserva-sala") 


