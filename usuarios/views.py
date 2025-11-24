from django.http import HttpResponse

def login_view(request):
    return HttpResponse('LOGIN SIMPLE - SITIO FUNCIONA')

def index_view(request):
    return HttpResponse('INDEX')
    
def registro_view(request):
    return HttpResponse('REGISTRO')
