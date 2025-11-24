from django.http import HttpResponse

def login_view(request):
    return HttpResponse('<h1>🔐 LOGIN</h1><form><input type=\"text\"><br><input type=\"password\"><br><button>Entrar</button></form>')

def index_view(request):
    return HttpResponse('<h1>🏠 INICIO</h1>')

def home(request):
    return HttpResponse('<h1>📱 HOME</h1>')
