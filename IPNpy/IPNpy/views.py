from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import json
from io import BytesIO  # Importa BytesIO desde el módulo io

def generate_pdf(conversation):
    # Creamos un objeto BytesIO para almacenar el PDF en memoria
    buffer = BytesIO()

    # Creamos un documento PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Convertimos la conversación de JSON a una lista de Python
    conversation_list = json.loads(conversation)

    # Creamos una lista de filas para la tabla del PDF
    data = [['Sender', 'Message']]
    for message in conversation_list:
        data.append([message['sender'], message['message']])

    # Creamos la tabla del PDF
    table = Table(data)

    # Estilizamos la tabla
    style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.gray),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0,0), (-1,0), 12),
                        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                        ('GRID', (0,0), (-1,-1), 1, colors.black)])

    table.setStyle(style)

    # Construimos la tabla y la agregamos al documento PDF
    elements = [table]
    doc.build(elements)

    # Obtén el contenido del buffer y devuelve una respuesta de tipo PDF
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def index(request):
    if request.method == 'GET':
        # Definimos cada mensaje de la conversación como variables individuales
        message1 = {"sender": "Persona", "message": "Hola, bot. ¿Cómo estás?"}
        message2 = {"sender": "Bot", "message": "¡Hola! Estoy bien, gracias por preguntar."}
        message3 = {"sender": "Persona", "message": "¿Qué has estado haciendo últimamente?"}
        message4 = {"sender": "Bot", "message": "He estado ayudando a resolver preguntas interesantes."}
        message5 = {"sender": "Persona", "message": "¡Eso suena genial!"}
        message6 = {"sender": "Bot", "message": "Sí, es bastante divertido."}
        message7 = {"sender": "Persona", "message": "Bueno, hasta luego."}
        message8 = {"sender": "Bot", "message": "Adiós, que tengas un buen día."}

        # Creamos una lista de mensajes JSON usando las variables definidas
        conversation = [
            message1,
            message2,
            message3,
            message4,
            message5,
            message6,
            message7,
            message8
        ]

        # Convertimos la lista de mensajes JSON en una cadena JSON
        conversation_json = json.dumps(conversation)

        # Generamos el contenido del PDF
        pdf_content = generate_pdf(conversation_json)

        # Devolvemos el PDF como una respuesta HTTP
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="conversation.pdf"'
        return response
    else:
        return HttpResponse("Método no permitido", status=405)
