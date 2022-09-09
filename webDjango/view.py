from django.http import HttpResponse
from django.template import loader
def home (request):
    return HttpResponse("Hola soy la pagina Home")

def homePage(self):
    lista=[1,2,3,4,5,6,7,8,9]
    data = {'nombre': 'Santiago', 'apellido': 'Piglioni', 'lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)