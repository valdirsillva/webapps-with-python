from django.shortcuts import render
from .forms import EquationForm
from .calculate.SquareSolver import squareSolver
 
def index(request):
    if request.method == 'GET':
        form = EquationForm()
        context = { 'form': form }
        return render(request, 'form.html', context=context)
    else:
        form = EquationForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['value_a']
            b = form.cleaned_data['value_b']
            c = form.cleaned_data['value_c']

            results = squareSolver(a, b, c)

        return render(request, 'form.html', context={ 'form': form, 'r1': results[0], 'r2': results[1] })
