from django.shortcuts import render, redirect
from .forms import Clase1Form, Clase2Form, Clase3Form

def formulario(request):
    if request.method == 'POST':
        form1 = Clase1Form(request.POST)
        form2 = Clase2Form(request.POST)
        form3 = Clase3Form(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('formulario')
    else:
        form1 = Clase1Form()
        form2 = Clase2Form()
        form3 = Clase3Form()
    return render(request, 'formulario.html', {'form1': form1, 'form2': form2, 'form3': form3})

from django.shortcuts import render, redirect
from .forms import Clase1Form, Clase2Form, Clase3Form

def formulario(request):
    if request.method == 'POST':
        form1 = Clase1Form(request.POST)
        form2 = Clase2Form(request.POST)
        form3 = Clase3Form(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('formulario')
    else:
        form1 = Clase1Form()
        form2 = Clase2Form()
        form3 = Clase3Form()
    return render(request, 'formulario.html', {'form1': form1, 'form2': form2, 'form3': form3})

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line()
