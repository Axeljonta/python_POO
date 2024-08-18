#El Principio de Abierto/Cerrado (OCP), parte de los principios SOLID, establece que las 
# clases deben estar abiertas para la extensión, pero cerradas para la modificación. 
# Esto significa que debemos poder agregar nuevas funcionalidades al sistema (extenderlo) 
# sin tener que modificar el código existente. El objetivo es evitar que el código que ya 
# funciona bien se vea afectado por nuevos cambios, reduciendo el riesgo de introducir 
# errores.

# Clase base que lanza NotImplementedError si no se implementa enviar
class Notificacion:
    
    def __init__(self, mensaje,usuario):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError

# Subclase para notificaciones por WhatsApp
class WhatsAppNotificacion(Notificacion):
    def notificar(self):
        print(f"Enviando WhatsApp a usuario: {self.usuario} mensaje: {self.mensaje}")
# Subclase para notificaciones por Email
class EmailNotificacion(Notificacion):
    def notificar(self):
        print(f"Enviando Email a usuario: {self.usuario} mensaje: {self.mensaje}")

# Subclase para notificaciones por SMS
class SMSNotificacion(Notificacion):
    def notificar(self):
        print(f"Enviando SMS a usuario: {self.usuario} mensaje: {self.mensaje}")

# Uso:
whatsapp = WhatsAppNotificacion("Hola, este es tu mensaje de WhatsApp", "Axel")
email = EmailNotificacion("Este es tu mensaje de email", "Axel")
sms = SMSNotificacion("Este es tu mensaje de SMS", "Axel")

# Enviar notificaciones
whatsapp.notificar()
email.notificar()
sms.notificar()