from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = 'EAA6LJPGCxHsBPOVJU6yzdwpAAy7L3GVTevTU1WXfG2BU47piv4BU66WBhwQcmXMnUrWDZA5xGif7AvKzsQkNilIQmE4OZAUVavNbNPJMZBk0ooFpdZCXmlKToHQyp6A7IZBEwiuFfvuMyfWrmiBkTNuaIXwGDFuI0MyUmIZCaZAbZBaHEMYJcrzLZCJeMnj5hYROo'
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
        texto =  data.get("mensaje") 
        #mensaje = data.get("question", texto)  # mensaje por defecto
        telefono = '541125123781'  # Número fijo

        payload = {
            "messaging_product": "whatsapp",
            "to": telefono,
            "type": "text",
            "text": {
                "body": texto
            }
        }

        response = requests.post(WHATSAPP_URL, headers=HEADERS, json=payload)

        if response.status_code != 200:
            return jsonify({"error": "Error al enviar mensaje", "detalle": response.json()}), 500

        return jsonify({"status": "Mensaje enviado correctamente", "mensaje": texto}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
