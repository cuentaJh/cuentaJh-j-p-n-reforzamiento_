from django.shortcuts import render
from pokemon.models import Pokemon

# Create your views here.

def pokemon_list(request):
    data_contex = {
        'nombre': 'Pokemon1',
        'numero': 24,
        'generacion': 'Gen1',
        'tipo': 'Fuego'
    }

    return render(request,'pokemon_list.html', context={'data': data_contex})


def pokemon_orm(request):
    data_context = []

    data_context = Pokemon.objects.filter(tipo='Fuego')

    return render(request, 'pokemon_orm.html', context={'data': data_context})