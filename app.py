# -*- coding: utf-8 -*-
import os
from flask import Flask, jsonify, request
from heyoo import WhatsApp

app = Flask(__name__)

# EJECUTAMOS ESTE CODIGO CUANDO SE INGRESE A LA RUTA ENVIAR
@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    # Obtener credenciales de variables de entorno
    # TOKEN DE ACCESO DE FACEBOOK
    token = os.environ.get('WHATSAPP_TOKEN')
    # IDENTIFICADOR DE NUMERO DE TELEFONO
    idNumeroTelefono = os.environ.get('WHATSAPP_PHONE_ID')
    # TELEFONO QUE RECIBE MENSAJE (el que diste de alta en Meta)
    telefonoEnvia = os.environ.get('WHATSAPP_RECIPIENT')

    # Validacion: Asegurarse que las variables de entorno estan configuradas
    if not token or not idNumeroTelefono or not telefonoEnvia:
        error_msg = "Faltan configurar variables de entorno: WHATSAPP_TOKEN, WHATSAPP_PHONE_ID, WHATSAPP_RECIPIENT."
        print(f"ERROR: {error_msg}")
        return jsonify({"error": error_msg}), 500

    # MENSAJE A ENVIAR (estos pueden seguir hardcodeados o hacerse dinamicos en el futuro)
    textoMensaje="Hola novato saludos"
    # URL DE LA IMAGEN A ENVIAR
    urlImagen='https://i.imgur.com/r5lhxgn.png'

    try:
        # INICIALIZAMOS ENVIO DE MENSAJES
        mensajeWa = WhatsApp(token, idNumeroTelefono)
        
        # ENVIAMOS UN MENSAJE DE TEXTO
        print(f"Intentando enviar mensaje a {telefonoEnvia}...")
        mensajeWa.send_message(textoMensaje, telefonoEnvia)
        
        # ENVIAMOS UNA IMAGEN
        print(f"Intentando enviar imagen a {telefonoEnvia} desde {urlImagen}...")
        mensajeWa.send_image(image=urlImagen, recipient_id=telefonoEnvia)
        
        print("Mensajes enviados exitosamente.")
        return "mensaje enviado exitosamente"
    except Exception as e:
        print(f"Error al enviar mensaje por WhatsApp: {e}")
        return jsonify({"error": f"Error al enviar mensaje por WhatsApp: {str(e)}"}), 500

# No se necesita el bloque if __name__ == "__main__": app.run(debug=True) en produccion
# Gunicorn se encargara de iniciar la aplicacion.