
from flask import Flask, jsonify, request
from heyoo import WhatsApp
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

@app.after_request
def set_charset(response):
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


# EJECUTAMOS ESTE CODIGO CUANDO SE INGRESE A LA RUTA ENVIAR
@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    # TOKEN DE ACCESO DE FACEBOOK
    token='EAA6LJPGCxHsBO9SL7SCBViAOjReFO4bID0pFKZA6vCIsABA3TcSoCH7FsjwXjnNKrRYCqvNAmePkF8GPC4IU4ZBQZAoLe7cHZAnvWDag44hB27D8ZAvGkptmrYZAXDYGK2CmyJAGppiVpOZB3FhreqZA9DslEyFomMNQQoGcQ2ZBxdZA4YZAxnxnDXx5ZBvZAGx3Xs16hZAjtIaz4HNG2jFZBPVHMmYBG5OBcXHMZCTxlrZBKoT841HsKAEIZD'
    # IDENTIFICADOR DE NUMERO DE TELEFONO
    idNumeroTelefono='651005361434016'
    # TELEFONO QUE RECIBE MENSAJE (el que diste de alta en Meta)
    telefonoEnvia='541125123781'

    # MENSAJE A ENVIAR
    textoMensaje="Hola novato saludos"
    # URL DE LA IMAGEN A ENVIAR
    urlImagen='https://i.imgur.com/r5lhxgn.png'

    try:
        # INICIALIZAMOS ENVIO DE MENSAJES
        mensajeWa = WhatsApp(token, idNumeroTelefono)
        
        # ENVIAMOS UN MENSAJE DE TEXTO
        print(f"Intentando enviar mensaje a {telefonoEnvia}")
        mensajeWa.send_message(textoMensaje, telefonoEnvia)
        
        # ENVIAMOS UNA IMAGEN
        print(f"Intentando enviar imagen a {telefonoEnvia} desde {urlImagen}")
        mensajeWa.send_image(image=urlImagen, recipient_id=telefonoEnvia)
        
        print("Mensajes enviados exitosamente")
        return "mensaje enviado exitosamente"
    except Exception as e:
        print(f"Error al enviar mensaje por WhatsApp: {e}")
        return jsonify({"error": f"Error al enviar mensaje por WhatsApp: {str(e)}"}), 500

if __name__ == "__main__": 
    app.run(debug=True)
