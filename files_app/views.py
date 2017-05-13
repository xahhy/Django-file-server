from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404

from .models import *
# Create your views here.
def home(request):
    pass

def download(request,id):
    object_name = get_object_or_404(FilesModel,pk=id)
    print(id)
    print(object_name)
    filename = object_name.file.path.split('/')[-1]
    print(filename)
    response = HttpResponse(object_name.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response