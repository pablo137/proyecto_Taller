from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from producto.models import Productos
# Create your views here.
@login_required
def perfil(request):
    try:
        productos = Productos.objects.filter(user=request.user)
        context = {'titulo': 'Perfil',
               'productos': productos}
        return render(request, 'perfil.html',context)
    except Productos.DoesNotExist:
        return render(request, 'perfil.html',{'titulo': 'Perfil',
                                              'productos': False})
                # 'productos': request.user.producto.project_set.all()}
    # return render(request, 'perfil.html',context)