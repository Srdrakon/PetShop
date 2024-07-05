from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from PetApp.forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True})
        else:
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
