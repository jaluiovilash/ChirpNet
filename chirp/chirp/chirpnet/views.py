from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .models import ChirpNet
from .forms import ChirpNetForm, UserRegistrationForm


# Create your views here.
def index(request):
    return render(request, 'index.html');
    

def chirpnet_list(request):
    chirps = ChirpNet.objects.all().order_by('-created_at');
    return render(request, 'chirpnet_list.html', {'chirps':chirps});


@login_required
def chirpnet_create(request):
    if request.method == 'POST':
        form = ChirpNetForm(request.POST,request.FILES);
        if form.is_valid():
            chirpnet = form.save(commit = False);
            chirpnet.user = request.user;
            chirpnet.save();
            return redirect('chirpnet_list');
    else:
        form = ChirpNetForm();
    return render(request, 'chirpnet_form.html',{'form':form});


@login_required
def chirpnet_edit(request, chirpnet_id):
    chirpnet = get_object_or_404(ChirpNet, pk = chirpnet_id, user = request.user);
    if request.method == 'POST':
        form = ChirpNetForm(request.POST,request.FILES, instance = chirpnet);
        if form.is_valid():
            chirpnet = form.save(commit = False);
            chirpnet.user = request.user;
            chirpnet.save();
            return redirect('chirpnet_list');
    else:
        form = ChirpNetForm(instance=chirpnet);
    return render(request, 'chirpnet_form.html',{'form':form});


@login_required
def chirpnet_delete(request, chirpnet_id):
    chirpnet = get_object_or_404(ChirpNet, pk = chirpnet_id, user = request.user);
    if request.method == 'POST':
        chirpnet.delete();
        return redirect('chirpnet_list');
    return render(request, 'chirpnet_confirm_delete.html',{'chirpnet':chirpnet});


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST);
        if form.is_valid():
            user = form.save(commit=False);
            user.set_password(form.cleaned_data['password1']);
            user.save();
            login(request, user);
            return redirect('chirpnet_list');
    else:
        form = UserRegistrationForm();
    return render(request, 'registration/register.html',{'form':form});
