from django.shortcuts import render
from owner.models import Owner

# Create your views here.

def owner_list(request):

    data_contex ={
            'nombre': 'Luis Pardo',
            'edad': 24,
            'pais': 'Perú',
        }


    return render(request,'owner_list.html', context={'data': data_contex})


def owner_orm(request):
    data_context = []

    data_context = Owner.objects.filter(pais='Perú')

    return render(request, 'owner_orm.html', context={'data': data_context})