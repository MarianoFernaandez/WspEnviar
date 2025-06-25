import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = 'TU_TOKEN_DE_ACCESO'
PHONE_NUMBER_ID = 'TU_PHONE_NUMBER_ID'
WHATSAPP_URL = f'https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages'
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@app.route('/enviar/', methods=['POST', 'GET'])
def enviar():
    telefono = '541125123781'
    texto = 'Hola novato saludos'
    imagen_url = 'https://i.imgur.com/r5lhxgn.png'

    try:
        # Enviar texto
        data_texto = {
            "messaging_product": "whatsapp",
            "to": telefono,
            "type": "text",
            "text": {
                "body": texto
            }
        }
        response_texto = requests.post(WHATSAPP_URL, headers=HEADERS, json=data_texto)
        response_texto.raise_for_status()

        # Enviar imagen
        data_imagen = {
            "messaging_product": "whatsapp",
            "to": telefono,
            "type": "image",
            "image": {
                "link": imagen_url
            }
        }
        response_imagen = requests.post(WHATSAPP_URL, headers=HEADERS, json=data_imagen)
        response_imagen.raise_for_status()

        return jsonify({"mensaje": "Mensajes enviados exitosamente"}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
