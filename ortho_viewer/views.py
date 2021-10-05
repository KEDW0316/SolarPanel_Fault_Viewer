from django.contrib.auth import get_backends
from django.http.response import HttpResponseRedirect
from ortho_viewer.faultform import FaultForm
from ortho_viewer.models import Orthoimage, panel_fault
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from ortho_viewer.models import Orthoimage,panel_fault
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    orthoimage=Orthoimage.objects.all()
    return render(request, 'ortho_viewer/index.html' , {'orthoimage': orthoimage})

def more(request):
    return render(request, 'ortho_viewer/more.html')

def login(request):
    return render(request, 'ortho_viewer/login.html')

def more(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    panelfault = panel_fault.objects.all()
    return render(request, 'ortho_viewer/more.html', {'orthoimage':orthoimage, 'panelfault':panelfault})

def faultform(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    return render(request, 'ortho_viewer/fault_form.html', {'orthoimage':orthoimage})

@csrf_exempt
def create(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    fault=panel_fault()
    fault.image_id=orthoimage
    fault.px_x=request.POST['px_x']
    fault.px_y=request.POST['px_y']
    fault.fault_image=request.FILES['fault_image']
    fault.save()
    return redirect('/more/'+str(orthoimage.id))

# Create your views here.
