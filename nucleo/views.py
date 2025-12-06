from django.shortcuts import render
from django.conf import settings

ARCHIVOS = [
    {"nombre": "f.pdf", "ruta": settings.MEDIA_URL + "files/f.pdf", "tipo": "pdf"},
    {"nombre": "Documento (2).docx", "ruta": settings.MEDIA_URL + "files/Documento (2).docx", "tipo": "docx"},
    {"nombre": "Infografía PIP", "ruta": settings.MEDIA_URL + "files/imagen_pip.jpg", "tipo": "imagen"},
    {"nombre": "Enlace externo", "ruta": "https://youtu.be/TXlJoF5SeiU", "tipo": "link"},
]

def inicio(request):
    return render(request, "nucleo/index.html", {"archivos": ARCHIVOS})

