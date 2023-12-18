from django.shortcuts import render

# Create your views here.

def pokemon_list(request):
    data_contex = {
        'nombre': 'Pokemon1',
        'numero': 24,
        'generacion': 'Gen1',
        'tipo': 'Fuego'
    }

    return render(request,'pokemon_list.html', context={'data': data_contex})
