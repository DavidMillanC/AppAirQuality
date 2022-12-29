import pywhatkit

def enviarMensaje(msg, hour, min):
    try:
        pywhatkit.sendwhatmsg("+593978632085",msg, hour,min)
        print("Enviado correctamente!")
    except:
        print("Oh oh!! Problemas con el envío del mensaje")