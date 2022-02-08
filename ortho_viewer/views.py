from django.contrib.auth import get_backends
from django.http.response import HttpResponseRedirect
from ortho_viewer.faultform import FaultForm
from ortho_viewer.models import Orthoimage, panel_fault
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from ortho_viewer.models import Orthoimage,panel_fault
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def panorama(request):
    return render(request, 'panorama/index.html')

def index(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        if cur_user.is_superuser:
            orthoimage=Orthoimage.objects.all()
        else:
            orthoimage=Orthoimage.objects.filter(user_id=cur_user)
            
        return render(request, 'ortho_viewer/index.html' , {'orthoimage': orthoimage})
    else:
        return redirect('login')
def gohome(request):
    return redirect('index')

def more(request):
    return render(request, 'ortho_viewer/more.html')

def more(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    panelfault = panel_fault.objects.filter(image_id=orthoimage)
    cur_user=request.user
    
    if cur_user.is_superuser:
        is_super = True
    else : 
        is_super = False
    return render(request, 'ortho_viewer/more.html', {'orthoimage':orthoimage, 'panelfault':panelfault, 'superuser':is_super})

def faultform(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    panelfault = panel_fault.objects.filter(image_id=orthoimage)

    return render(request, 'ortho_viewer/fault_form.html', {'orthoimage':orthoimage, 'panelfault':panelfault})

@csrf_exempt
def create(request, pk):
    orthoimage = get_object_or_404(Orthoimage, pk=pk)
    fault=panel_fault()
    fault.image_id=orthoimage
    fault.px_x=request.POST['px_x']
    fault.px_y=request.POST['px_y']
    fault.fault_image=request.FILES['fault_image']
    fault.fault_type=request.POST['fault_type']
    fault.save()
    return redirect('/more/'+str(orthoimage.id))

@csrf_exempt
def create_faultmark(request, pk, pk2):
    fault = get_object_or_404(panel_fault, pk=pk)
    orthoimage = get_object_or_404(Orthoimage, pk=pk2)

    fault.fault_x=request.POST['fault_x']
    fault.fault_y=request.POST['fault_y']
    fault.fault_width=request.POST['fault_width']
    fault.fault_height=request.POST['fault_height']
    fault.save(update_fields=["fault_x","fault_y","fault_width","fault_height"])
    return redirect('/more/'+str(orthoimage.id))
# Create your views here.
