# Create your views here.
from django.shortcuts import render_to_response
from django_facebook.decorators import facebook_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context import RequestContext
from django_facebook.api import get_persistent_graph
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse

def home(request):
    context = RequestContext(request)

    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        fb = get_persistent_graph(request)
        fb.set('323555591081578/feed', message = mensaje)
        return HttpResponseRedirect('/')
    return render_to_response('home.html', context)

@facebook_required(scope='publish_stream')
#@facebook_required(scope='manage_pages, publish_stream')
#@csrf_protect
def enviarApagina(request):
    context = RequestContext(request)
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        fb = get_persistent_graph(request)
        fb.set('323555591081578/feed', message = mensaje)
        return HttpResponseRedirect('/')
    return render_to_response('home.html', context)