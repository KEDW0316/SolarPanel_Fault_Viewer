from ortho_viewer.models import Orthoimage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ortho_viewer.models import Orthoimage

def index(request):
    orthoimage=Orthoimage.objects.all()
    return render(request, 'ortho_viewer/index.html' , {'orthoimage': orthoimage})

def more(request):
    return render(request, 'ortho_viewer/more.html')

def login(request):
    return render(request, 'ortho_viewer/login.html')

def more(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    return render(request, 'ortho_viewer/more.html', {'orthoimage':orthoimage})


# Create your views here.
