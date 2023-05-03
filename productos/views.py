from re import template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from productos.forms import IngresarProductoForm, ModificarStockForm



# Create your views here.
#Tupla producto: (id_producto, nombre, fabricante, stock)
listaProductos=[
    (1,'prod A','fabricante1',32),
    (2,'prod B','fabricante1',0),
    (3,'prod C','fabricante1',5),
    (4,'prod D','fabricante1',65),
    (5,'prod E','fabricante1',9),
    (6,'prod A','fabricante1',32),
    (7,'prod B','fabricante1',0),
    (8,'prod C','fabricante1',5),
    (9,'prod D','fabricante1',65),
    (10,'prod E','fabricante1',9),
    ]

#Tupla fabricante: (id_fabricante, nombre, direccion,telefono, mail)
listaFabricantes=[
    (1,'fabricante1', "calle1", '4900-0000', 'mail@mail.com'),
    (2,'fabricante2', "calle1", '4900-0000', 'mail@mail.com'),
    (3,'fabricante3', "calle1", '4900-0000', 'mail@mail.com'),
    (4,'fabricante4', "calle1", '4900-0000', 'mail@mail.com'),
    ]


def productos_mostrar(request):
    template = loader.get_template('productos/productos.html')
    context={'productos':listaProductos}
    return HttpResponse(template.render(context,request))

def producto_nuevo(request):
    template = loader.get_template('productos/producto_nuevo.html')
    context={'IngresarProductoForm':IngresarProductoForm}
    return HttpResponse(template.render(context,request))
    #return render(request,'productos/producto_nuevo.html')

def producto_editar(request,id_prod):
    template = loader.get_template('productos/producto_editar.html')
    context={'id_item':id_prod}
    return HttpResponse(template.render(context,request))

def fabricantes_mostrar(request):
    template = loader.get_template('productos/fabricantes.html')
    context={'fabricantes':listaFabricantes}
    return HttpResponse(template.render(context,request))
    
def fabricante_editar(request,id_fabr):
    template = loader.get_template('productos/fabricante_editar.html')
    context={'id_fabricante':id_fabr}
    return HttpResponse(template.render(context,request))

def fabricante_nuevo(request):
    #template = loader.get_template('productos/fabricante_nuevo.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    return render(request,'productos/fabricante_nuevo.html')

def stock(request):
    template = loader.get_template('productos/modificar_stock.html')
    context={'ModificarStockForm':ModificarStockForm}
    return HttpResponse(template.render(context,request))
    #template = loader.get_template('productos/modificar_stock.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    #return render(request,'productos/modificar_stock.html')

def ver_facturas(request):
    #template = loader.get_template('productos/facturas.html')
    #context={'':}
    #return HttpResponse(template.render(context,request))
    return render(request,'productos/facturas.html')
