# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = services.getAllImages() #uso la funcion que ya complete, obtengo los pokemon
    favourite_list = services.getAllFavourites(request) if request.user.is_authenticated else [] #si mas adelante hago favoritos, dejo la funcion ya hecha

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

# función utilizada en el buscador.
def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        images = services.filterByCharacter(name) #llama a la función que cree en services.py
        # y devulve una lista de pokemons filtrada por el texto que se ingresó
        favourite_list = services.getAllFavourites(request) if request.user.is_authenticated else [] #si el usuario está logueado, carga la lista de favoritos,sino devuelve una lista vacía

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por el tipo del Pokemon
def filter_by_type(request):
    type = request.POST.get('type', '')

    if type != '':
        images = services.filterByType(type) #llama a la función que cree en services.py 
        #devulve lista de pokemons filtados por el tipo que se ingreso
        #me aseguro que devuelva lista vacia ya que no va a haber ingreso de usuario.
        favourite_list = services.getAllFavourites(request) if request.user.is_authenticated else [] 

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home') 

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    pass

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')