from django.shortcuts import render

# Create your views here.

def owner_list(request):

    data_contex = {
        'nombre': 'Luis Pardo',
        'edad': 24,
        'pais': 'Perú',
    }

    return render(request,'owner_list.html', context={'data': data_contex})
