# import requests
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# TOKEN = 'EAA6LJPGCxHsBOxXVnSMdvwf7XKDnLSmEXdYy2pTdWEVntEEJD8OZCuMoO7wIrBSiSQfLYUlinQBEFsxZBs4coFGr1BGE5jZBFmOEVTIHhoEPoFp1GAFxAdOdoC2ATvenFb7VKcCLZC0ehAv0tqPnyBCifuK8AB5sT4puZAiGZC5VCy7eNBpCZCUaggJJAnZAymFWjLdKZBnxpX62tUZAcq5QQWrdj2XrV5qfUB2McJo4MyGMuEak4ZD'
# PHONE_NUMBER_ID = '651005361434016'
# WHATSAPP_URL = f'https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages'
# HEADERS = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Content-Type": "application/json"
# }

# @app.route('/enviar/', methods=['POST', 'GET'])
# def enviar():
#     telefono = '541125123781'
#     texto = 'Hola novato saludos'

#     try:
#         # Enviar texto
#         data_texto = {
#             "messaging_product": "whatsapp",
#             "to": telefono,
#             "type": "text",
#             "text": {
#                 "body": texto
#             }
#         }
#         response_texto = requests.post(WHATSAPP_URL, headers=HEADERS, json=data_texto)
#         response_texto.raise_for_status()

#         # Enviar imagen
#         data_imagen = {
#             "messaging_product": "whatsapp",
#             "to": telefono,
#             "type": "image",
#             "image": {
#                 "link": imagen_url
#             }
#         }
#         response_imagen = requests.post(WHATSAPP_URL, headers=HEADERS, json=data_imagen)
#         response_imagen.raise_for_status()

#         return jsonify({"mensaje": "Mensajes enviados exitosamente"}), 200

#     except requests.exceptions.RequestException as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == '__main__':
#     # Ejecutar servidor
#     app.run(debug=True)

#     # Enviar mensaje cuando arranca
#     with app.app_context():
#         enviar()

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = 'EAA6LJPGCxHsBOxXVnSMdvwf7XKDnLSmEXdYy2pTdWEVntEEJD8OZCuMoO7wIrBSiSQfLYUlinQBEFsxZBs4coFGr1BGE5jZBFmOEVTIHhoEPoFp1GAFxAdOdoC2ATvenFb7VKcCLZC0ehAv0tqPnyBCifuK8AB5sT4puZAiGZC5VCy7eNBpCZCUaggJJAnZAymFWjLdKZBnxpX62tUZAcq5QQWrdj2XrV5qfUB2McJo4MyGMuEak4ZD'
PHONE_NUMBER_ID = '651005361434016'
WHATSAPP_URL = f'https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages'
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@app.route('/enviar/', methods=['POST'])
def enviar():
    try:
        data = request.get_json()
        mensaje = data.get("question", "Hola desde la API")  # mensaje por defecto si no se envía nada
        telefono = '541125123781'  # Número fijo o configurable si querés

        # Enviar texto por WhatsApp
        data_texto = {
            "messaging_product": "whatsapp",
            "to": telefono,
            "type": "text",
            "text": {
                "body": mensaje
            }
        }

        response = requests.post(WHATSAPP_URL, headers=HEADERS, json=data_texto)
        response.raise_for_status()

        return jsonify({"status": "Mensaje enviado correctamente", "mensaje": mensaje}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
