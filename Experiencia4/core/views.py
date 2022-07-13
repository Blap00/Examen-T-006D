import datetime
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render , redirect
from django.forms.models import model_to_dict
from django.db.models import F
from .models import *
from .forms import RegisterForm 

def index(request):
    context = {} 
    context['mensaje']=''
    context['mensajeLogin']=''
    context['registro_vacio'] = False
    context['esta_registrado'] = False
    context['esta_logueado'] = False
    context['error_login'] = False
    if request.method == 'GET':
        if 'error_login' in request.session:
            if request.session['error_login']:
               context['error_login'] = True 
               request.session['error_login'] = False
        if 'user' in request.session:
            context['esta_logueado'] = True
            context['Usuario'] = request.session['user']
        return render(request, 'core/index.html', context)
    elif request.method == 'POST':
        if 'user' in request.session:
            context['esta_logueado'] = True
        data = dict(request.POST)
        if 'registrar-btn' in data:
            username = data['usernameRegistro'][0]
            email = data['emailRegistro'][0]
            password = data['passwordRegistro'][0]
            user = Usuarios(username,email,password)
            if Usuarios.objects.filter(username = user.username).exists():
                context['esta_registrado']=True
                context['mensaje']='El usuario ya existe'
                return render(request, 'core/index.html', context)
            elif Usuarios.objects.filter(mail = user.mail).exists():
               context['esta_registrado']=True
               context['mensaje']='El correo ya esta registrado'
               return render(request, 'core/index.html', context)
            elif ['',] in data.values():
                print('error elif vacio registrar')
                context['registro_vacio'] = True
                context['mensajeRegistro']='No pueden haber campos vaci­os'
                return render(request, 'core/index.html', context)
            else:
                user.save()
            print(username, email, password)
        elif 'login-btn' in data:
            username = data['username'][0]
            password = data['password'][0]
            if Usuarios.objects.filter(username = username, password = password).exists():
                with Usuarios.objects.get(username = username) as user:
                    request.session['user'] = model_to_dict(user)
                context['esta_logueado'] = True
                request.session['error_login'] = False
                print('login correcto')
            else:
                request.session['error_login'] = True
                context['mensajeLogin'] = 'Datos ingresados no existen.'
                print('login incorrecto')
            print('logueando')
        elif'changepass' in data:
            password = data['contrasenaNueva'][0]
            user = Usuarios.objects.get(mail = request.session['mailChangePassword'])
            user.password = password
            user.save()
            del request.session['mailChangePassword']
        else:
            print('error')            
        return HttpResponseRedirect('/')

def logout(request):
    request.session.flush()
    request.session['carrito'] = {}
    response = JsonResponse({'success': 'Sesion cerrada'})
    response.status_code = 200
    HttpResponseRedirect('/')
    return response

def validacionRegistrar(request):
    context = {}
    context['registro_vacio'] = False
    data = dict(request.POST)
    username = data['usernameRegistro']
    email = data['emailRegistro']
    password = data['passwordRegistro']
    user = Usuarios(username,email,password)
    if '' in data.user.values():
        print('FUNCIONO')
        context['mensajeRegistro'] = 'Porfavor, ingresa datos para registrar'
        context['registro_vacio'] = True
    else:
        context['registro_vacio'] = False
    return HttpResponseRedirect('/')

def contactanos(request):
    return render(request, 'core/contactanos.html')

def Caninos(request):
    return render(request, 'core/GaCaninos.html')

def Felinos(request):
    return render(request, 'core/GaFelinos.html')

def Aves(request):
    return render(request, 'core/GaAves.html')

def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')

def registrarSolicitud(request):
    datos = {
        'form' : FormSolicitud()
    }
    if request.method == 'POST':
        data = dict(request.POST)
        nombre = data['nombreEntrada'][0]
        mail = data['emailEntrada'][0]
        descripcion = data['descripcionEntrada'][0]
        formulario = FormSolicitud(nombreCompleto = nombre, mailSolicitante = mail, descripcion = descripcion)
        formulario.save()
    return render(request, 'core/registrarSolicitud.html', datos)

def inicioSesion(request):
    return render(request, 'core/inicioSesion.html')

def revisarSolicitudes(request):
    solicitudes = FormSolicitud.objects.all()
    datos = {
        'solicitudes': solicitudes
    }
    return render(request, 'core/revisarSolicitudes.html', datos)

def borrarSolicitud(request, id):
    solicitudes=FormSolicitud.objects.get(idSolicitud=id)
    solicitudes.delete()
    return HttpResponseRedirect('/revisarSolicitudes.html')
    #return request(to='revisarSolicitudes.html')
    #return render(request, 'core/revisarSolicitudes.html')

def perfil(request):

    contexto = {} 
    contexto['esta_logueado'] = False
    contexto['esta_suscrito'] = False
    if request.method == 'GET':
        if 'user' in request.session:
            contexto['esta_logueado'] = True
            contexto['Usuario'] = request.session['user']
             
    return render(request, 'core/perfil.html',contexto)
    
def borrarperfil(request):
    contexto = {} 
    contexto['esta_logueado'] = False
    data = dict(request.POST)
    print(request.method)
    if request.method == 'POST':
        if 'borroton' in data: 
            print(data)
            username = data['usernames'][0]
            email = data['email'][0]
            password = data['password'][0]
            user = Usuarios(username,email,password)
            if Usuarios(**request.session['user']) == user:
                Usuarios(**request.session['user']).delete()
                request.session.flush()
                request.session['carrito'] = {}
                print("pase el delete")
                return redirect(to="index")
        else:
            contexto['esta_logueado'] = True
            contexto['Usuario'] = request.session['user']
            print("error")
    return render(request,'core/index.html')

def suscripcion(request):
    if 'user' in request.session:
        usuario = Usuarios.objects.get(username = request.session['user']['username'])
        usuario.suscripcion = not usuario.suscripcion
        usuario.save()
        request.session['user'] = model_to_dict(usuario)
    return redirect(to='Perfil')

def resetPassword(request):
    context = {}
    context['esta_registrado'] = True
    context['editar'] = False
    if request.method == 'GET':
        print('test')
    elif request.method == 'POST':
        is_registered = Usuarios.objects.filter(mail = request.POST['email2']).exists()
        request.session['mailChangePassword'] = request.POST['email2']
        context['esta_registrado'] = is_registered
        if is_registered:
            context['editar'] = True
    return render(request, 'core/resetPassword.html', context)

def modperfil(request):
    if request.method == 'GET':
        context ={}
        context['form'] = RegisterForm(instance=Usuarios(**request.session['user']))
        user=Usuarios(**request.session['user'])
        context['Usuario']=user
    if request.method == 'POST':
        print(request.POST)
        context ={}
        form = RegisterForm(data=request.POST)
        context['form'] = form
        user = Usuarios(username = request.session['user']['username'], mail = request.POST['mail'], password = request.POST['password'])
        user.save()
        context['Usuario']=user
        request.session['user']=model_to_dict(user)
    return render(request,'core/ModPerfil.html',context)

def catalogo(request):
    cartas = CatalogoProduct.objects.all()
    datos = {
        'cartas': cartas
    }
    if request.method == 'POST':
        if CatalogoProduct.objects.filter(nombrePlanta = request.POST['nombre']).exists():
            cant = int(request.POST['cantidad'])
            plantaComprar = CatalogoProduct.objects.get(nombrePlanta = request.POST['nombre'])
            if  1 <= cant <= plantaComprar.stockPlanta:
                plantaComprar.stockPlanta -= cant
                plantaComprar.save()
                try:
                    if plantaComprar.nombrePlanta not in request.session['carrito']:
                        request.session['carrito'][plantaComprar.nombrePlanta] = {'cantidad':cant, 'precio_unitario':plantaComprar.precioPlanta}
                    else:
                        request.session['carrito'][plantaComprar.nombrePlanta]['cantidad'] += cant
                except KeyError as e:
                    request.session['carrito'] = {}
                    request.session['carrito'][plantaComprar.nombrePlanta] = {'cantidad':cant, 'precio_unitario':plantaComprar.precioPlanta}
    try: 
        datos['carrito'] = request.session['carrito']
    except KeyError as e:
        datos['carrito'] = {}
        request.session['carrito'] = {}
    try:
        suscrito = Usuarios.objects.get(username = request.session['user']['username']).suscripcion
    except Usuarios.DoesNotExist:
        suscrito = False
    if(suscrito):
        for key in datos['carrito']:
            datos['carrito'][key]['desc'] = -(datos['carrito'][key]['cantidad'] * datos['carrito'][key]['precio_unitario'])*0.05
    return render(request, 'core/catalogo.html', datos)

def limpiarCarroto(request):
    request.session['carrito'] = {}
    return redirect(to="Catalogo")

def boleton(request):
    if len(request.session['carrito']) == 0:
        return redirect(to="Catalogo")
    else:
        datos = {}
        datos['carrito'] = request.session['carrito']
        precioTotal = sum([int(j['cantidad']) * int(j['precio_unitario']) for i, j in request.session['carrito'].items()])
        descuento = int(request.session['descuento']) if 'descuento' in request.session else 0
        print('El descuento de la sesion es de ' + str(['descuento']))
        print('El descuento final es de ' + str(descuento))
        request.session['descuento'] = 0
        precioTotal1 = int(precioTotal - (precioTotal*(descuento)/100))
        boletita = boleta(precioTotal = precioTotal1, fecha = datetime.datetime.now())
        boletita.save()
        datos['boleta'] = boletita
        for key, value in request.session['carrito'].items():
            planta = CatalogoProduct.objects.get(nombrePlanta = key)
            planta.stockPlanta -= value['cantidad']
            planta.save()
        request.session['carrito'] = {}
        return render(request, 'core/boleta.html', datos)

def seguimiento(request):
    return render(request, 'core/seguimiento.html')



# Create your views here.datos
