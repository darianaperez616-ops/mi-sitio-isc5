from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuarios/login.html')

def index_view(request):
    return HttpResponse('INDEX')
    
def registro_view(request):
    return HttpResponse('REGISTRO')
