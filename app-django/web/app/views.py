from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
    # Pega todos os uauários do banco
    users = User.objects.all()

    context = {
       'users': users 
    }

    return render(request, 'index.html', context )

def create(request):
    # Verifica se o metodo é GET  

    if request.method == 'GET':
        form = UserForm() # Pega o formulário vazio

        # criando um contexto formulário
        context = {
            'form': form,
        }
        
         # Enviando o form para a view 
        return render(request, 'criar.html', context=context)    
    else:
        form = UserForm(request.POST)
        if form.is_valid():

            form.save() 
            return redirect(index)    


def update(request, user_id):
    # Pega usuário onde chave primaria for igual ao user_Id
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UserForm(data=request.POST,instance=user)

        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = UserForm(instance=user)

        context = { 'form': form }

        return render(request, 'criar.html', context=context)

def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()

    return redirect(index)
