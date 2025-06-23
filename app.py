# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
#LIBRERIAS PARA ENVIAR MENSAJES VIA WHTSAPP
from heyoo import WhatsApp

app = Flask(__name__)

#EJECUTAMOS ESTE CODIGO CUANDO SE INGRESE A LA RUTA ENVIAR
@app.route("/enviar/", methods=["POST", "GET"])
def enviar():
    #TOKEN DE ACCESO DE FACEBOOK
    token='EAA6LJPGCxHsBOzEyjcFZB7q5XZBfBEBLCEojLBZBjpCf8Sj34lmBtUOYdD6tZBs1OymHZB2OFd5Vvq0nZB6DGZCoPec7QDl2jkvnNeXezFA9iUq89KDH8v7wvKPP2U9Tdh7XQNu7FYZBiNPuBxCnGyLZBj5yCg0Yk1dY4dqiivvuZAikz5x5EVCoQZAZBvpM7vMEVqr7V8Ns181D0QFUsJcNVDwwuyBmPpmxKAIDO9f6cNCwC2cmDwZDZD'
    #IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono='651005361434016'
    #TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia='541125123781'
    #MENSAJE A ENVIAR
    textoMensaje="Hola novato saludos"
    #URL DE LA IMAGEN A ENVIAR
    urlImagen='https://i.imgur.com/r5lhxgn.png'

    #INICIALIZAMOS ENVIO DE MENSAJES
    mensajeWa=WhatsApp(token,idNumeroTeléfono)
    #ENVIAMOS UN MENSAJE DE TEXTO
    mensajeWa.send_message(textoMensaje,telefonoEnvia)
    #ENVIAMOS UNA IMAGEN
    mensajeWa.send_image(image=urlImagen,recipient_id=telefonoEnvia,)
    return "mensaje enviado exitosamente"


#INICIAMSO FLASK
if __name__ == "__main__":
    app.run(debug=True)