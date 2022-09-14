import pathlib
from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from pathlib import Path
path=Path(__file__).parent.resolve()
def home (request):
    doc=loader.get_template("home.html")
    doc2=doc.render()
    return HttpResponse(doc2)

def homePage(self):
    lista=[1,2,3,4,5,6,7,8,9]
    data = {'nombre': 'Santiago', 'apellido': 'Piglioni', 'lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)