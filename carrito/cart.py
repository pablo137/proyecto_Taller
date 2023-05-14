class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

    def add(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id" : producto.id,
                'nombre': producto.nombre,
                'cantidad': 1,
                'total': producto.precio,
                'img' : producto.img.url,
            }
        else:
            self.carrito[id]['cantidad'] += 1
            self.carrito[id]['total'] += producto.precio
        self.save()

    def save(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True
    
    def remove(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save()
    
    def decrementar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['total'] -= producto.precio

            if self.carrito[id]['cantidad'] <1: self.remove(producto)
            self.save()
    
    def clear(self):
        self.session['carrito'] = {}
        self.session.modified = True