import json
from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        conversation = [
            {"sender": "Persona", "message": "Hola, bot. ¿Cómo estás?"},
            {"sender": "Bot", "message": "¡Hola! Estoy bien, gracias por preguntar."},
            {"sender": "Persona", "message": "¿Qué has estado haciendo últimamente?"},
            {"sender": "Bot", "message": "He estado ayudando a resolver preguntas interesantes."},
            {"sender": "Persona", "message": "¡Eso suena genial!"},
            {"sender": "Bot", "message": "Sí, es bastante divertido."},
            {"sender": "Persona", "message": "Bueno, hasta luego."},
            {"sender": "Bot", "message": "Adiós, que tengas un buen día."}
        ]
        return JsonResponse({"conversation": conversation})
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
