from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import ChirpNet
from .forms import ChirpNetForm

# Create your views here.

def index(request):
    return render(request, 'index.html')
    

def chirpnet_list(request):
    chirps = ChirpNet.objects.all()
    return render(request, 'chirpnet_list.html', {'chirps':chirps});
    

def chirpnet_create(request):
    if request.method == 'POST':
        form = ChirpNetForm(request.POST,request.FILES);
        if form.is_valid():
            chirpnet = form.save(commit = False);
            chirpnet.user = request.user;
            chirpnet.save();
            return redirect('chirpnet_list');
    else:
        form=ChirpNetForm()
    return render(request, 'chirpnet_form.html',{'form':form})
    

def chirpnet_edit(request, chirpnet_id):
    chirpnet = get_object_or_404(ChirpNet, pk=chirpnet_id, user = request.user)
    if request.method == 'POST':
        form = ChirpNetForm(request.POST,request.FILES, instance=chirpnet)
        if form.is_valid():
            chirpnet = form.save(commit=False)
            chirpnet.user = request.user
            chirpnet.save()
            return redirect('chirpnet_list')
    else:
        form = ChirpNetForm(instance=chirpnet)
    return render(request, 'chirpnet_form.html',{'form':form})
    

def chirpnet_delete(request, chirpnet_id):
    chirpnet = get_object_or_404(ChirpNet, pk=chirpnet_id, user = request.user)
    if request.method == 'POST':
        chirpnet.delete()
        return redirect('chirpnet_list')
    return render(request, 'chirpnet_confirmm_delete.html',{'chirpnet':chirpnet})
