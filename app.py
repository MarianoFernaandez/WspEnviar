# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify, request
from heyoo import WhatsApp

app = Flask(__name__)

@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    token = os.environ.get('WHATSAPP_TOKEN')
    idNumeroTelefono = os.environ.get('WHATSAPP_PHONE_ID')
    telefonoEnvia = os.environ.get('WHATSAPP_RECIPIENT')

    if not token or not idNumeroTelefono or not telefonoEnvia:
        error_msg = "Faltan configurar variables de entorno: WHATSAPP_TOKEN, WHATSAPP_PHONE_ID, WHATSAPP_RECIPIENT."
        print(error_msg.encode('utf-8', errors='replace').decode('utf-8'))
        return jsonify({"error": error_msg}), 500

    textoMensaje = "Hola novato saludos"
    urlImagen = 'https://i.imgur.com/r5lhxgn.png'

    try:
        mensajeWa = WhatsApp(token, idNumeroTelefono)

        print(f"Intentando enviar mensaje a {telefonoEnvia}...".encode('utf-8', errors='replace').decode('utf-8'))
        mensajeWa.send_message(textoMensaje, telefonoEnvia)

        print(f"Intentando enviar imagen a {telefonoEnvia} desde {urlImagen}...".encode('utf-8', errors='replace').decode('utf-8'))
        mensajeWa.send_image(image=urlImagen, recipient_id=telefonoEnvia)

        print("Mensajes enviados exitosamente.".encode('utf-8', errors='replace').decode('utf-8'))
        return "mensaje enviado exitosamente"
    except Exception as e:
        error_msg = f"Error al enviar mensaje por WhatsApp: {e}"
        print(error_msg.encode('utf-8', errors='replace').decode('utf-8'))
        return jsonify({"error": error_msg}), 500
