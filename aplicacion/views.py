from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from aplicacion.models import *
from aplicacion.forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

#_____________________________________________________ Menú principal
def home(request):
    return render(request, 'aplicacion/home.html')

def sobreMi(request):
    return render(request, 'aplicacion/acerca_de_mi.html')

#_____________________________________________________ Detalles (Perro)
@login_required
def detallesPerro(request, id):
    perro = get_object_or_404(Perro, pk=id)
    contexto={'perro':perro}
    return render(request, 'aplicacion/detalles_perro.html', contexto)

#_____________________________________________________ Búsqueda (Perro)

@login_required
def buscarPerros(request):
    return render(request, 'aplicacion/buscar.html')

@login_required
def encontrarPerros(request):
    if request.GET['buscar']:
        patron=request.GET['buscar']
        perros=Perro.objects.filter(raza__icontains=patron)
        contexto={'perro_list':perros}
        return render(request, 'aplicacion/perro_list.html', contexto)

    contexto = {'perro_list':Perro.objects.all()}
    return render(request, 'aplicacion/buscar.html', contexto)

#_____________________________________________________ Perro

class PerroList(LoginRequiredMixin, ListView):
    model = Perro

class PerroCreate(LoginRequiredMixin, CreateView):
    model = Perro
    fields = '__all__'
    success_url = reverse_lazy('perros')

class PerroUpdate(LoginRequiredMixin, UpdateView):
    model = Perro
    fields = '__all__'
    success_url = reverse_lazy('perros')

class PerroDelete(LoginRequiredMixin, DeleteView):
    model = Perro
    fields = '__all__'
    success_url = reverse_lazy('perros')

#_____________________________________________________ Detalles (Celular)
@login_required
def detallesCelular(request, id):
    celular = get_object_or_404(Celular, pk=id)
    contexto={'celular':celular}
    return render(request, 'aplicacion/detalle_celular.html', contexto)

#_____________________________________________________ Celular
    
class CelularList(LoginRequiredMixin, ListView):
    model = Celular

class CelularCreate(LoginRequiredMixin, CreateView):
    model = Celular
    fields = '__all__'
    success_url = reverse_lazy('celulares')

class CelularUpdate(LoginRequiredMixin, UpdateView):
    model = Celular
    fields = '__all__'
    success_url = reverse_lazy('celulares')

class CelularDelete(LoginRequiredMixin, DeleteView):
    model = Celular
    fields = '__all__'
    success_url = reverse_lazy('celulares')

#_____________________________________________________ Detalles (Zapatilla)
@login_required
def detallesZapatilla(request, id):
    zapatilla = get_object_or_404(Zapatilla, pk=id)
    contexto={'zapatilla':zapatilla}
    return render(request, 'aplicacion/detalles_zapatilla.html', contexto)

#_____________________________________________________ Zapatilla
    
class ZapatillaList(LoginRequiredMixin, ListView):
    model = Zapatilla

class ZapatillaCreate(LoginRequiredMixin, CreateView):
    model = Zapatilla
    fields = '__all__'
    success_url = reverse_lazy('zapatillas')

class ZapatillaUpdate(LoginRequiredMixin, UpdateView):
    model = Zapatilla
    fields = '__all__'
    success_url = reverse_lazy('zapatillas')

class ZapatillaDelete(LoginRequiredMixin, DeleteView):
    model = Zapatilla
    fields = '__all__'
    success_url = reverse_lazy('zapatillas')

#_____________________________________________________ Detalles (Auto)
@login_required
def detallesAuto(request, id):
    auto = get_object_or_404(Auto, pk=id)
    contexto={'auto': auto}
    return render(request, 'aplicacion/detalles_auto.html', contexto)

#______________________________________________________ Auto

class AutoList(LoginRequiredMixin, ListView):
    model = Auto

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos')

#_______________________________________________________ Login, Logout, Authentication, Registration
    
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)

        if user is not None:
            login(request, user)

            #_________ Avatar
            try:
                avatar=Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar="/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            #_________________________________________________________

            return render(request, "aplicacion/home.html")
        else:
            redirect(reverse_lazy('login'))
    else:
        miForm=AuthenticationForm

        return render(request, 'aplicacion/login.html', {'miForm':miForm})

@login_required
def logout_request(request):
    logout(request)

    return redirect('home')

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = RegistroForm()
        
    return render(request, "aplicacion/registro.html", {"form":miForm})

#_________________________________________________________ Edición de Perfil, Cambio Clave, Avatar

def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    
    else:
        miForm = UserEditForm(instance=usuario)
    
    return render(request, "aplicacion/editarPerfil.html", {'form':miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy('home')

def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo)>0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #_____________________________________________________
            avatar = Avatar(user=usuario, 
                            imagen=miForm.cleaned_data["imagen"])

            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            print(f"{imagen}")

            return redirect(reverse_lazy('home'))
    
    else:
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form":miForm})