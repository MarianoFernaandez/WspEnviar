from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = 'EAA6LJPGCxHsBOyZCZCVML9MNkGGZCSYoRAHVQ28st1ZAUSX6zNJ5MA9c52fvsPLZBjLvBCkRJQwtzJ1umdE8zcsONkAAD5iS4MVO2NPtGifhGZAolend1ZAn6GnLGYr1GcemqFZBLRaBx8v3VgvnDUak8adFYLZCBAQLEKhEV0G6OjIcHZBj9oeLFJoQZA3QMwUZC6R42i9xIO6vZAiaJYQiR68h3PPcj45vh5xqbUnMITZBX3FJIZBBQZDZD'
PHONE_NUMBER_ID = '651005361434016'
WHATSAPP_URL = f'https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages'
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@app.route('/enviar/', methods=['POST'])
def enviar():
    try:
        if not request.is_json:
            return jsonify({"error": "La solicitud debe contener JSON"}), 400

        data = request.get_json()
        mensaje = data.get("question", "Hola desde la API")  # mensaje por defecto
        telefono = '541125123781'  # Número fijo

        payload = {
            "messaging_product": "whatsapp",
            "to": telefono,
            "type": "text",
            "text": {
                "body": mensaje
            }
        }

        response = requests.post(WHATSAPP_URL, headers=HEADERS, json=payload)

        if response.status_code != 200:
            return jsonify({"error": "Error al enviar mensaje", "detalle": response.json()}), 500

        return jsonify({"status": "Mensaje enviado correctamente", "mensaje": mensaje}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
