from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from producto.models import Productos
# Create your views here.
@login_required
def perfil(request):
    context = {'titulo': 'Perfil',
               'productos': Productos.objects.filter(id=request.user.id)}
                # 'productos': request.user.producto.project_set.all()}
    return render(request, 'perfil.html',context)