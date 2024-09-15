# Importamos la clase Pin del módulo machine
from machine import Pin

class ControladorLed:
    """
    Clase para controlar un LED conectado a un pin específico.
    
    Esta clase proporciona métodos para encender y apagar un LED.
    """

    def __init__(self, pin):
        """
        Inicializa el ControladorLed.
        
        Args:
            pin (int): El número del pin al que está conectado el LED.
        """
        # Guardamos el número del pin como un atributo privado
        self.__pin = pin
        # Creamos un objeto Pin configurado como salida
        self.led = Pin(self.__pin, Pin.OUT)
    
    def enciende_led(self):
        """
        Enciende el LED.
        
        Establece el valor del pin en 1 (alto) para encender el LED.
        """
        self.led.value(1)
        
    def apagar_led(self):
        """
        Apaga el LED.
        
        Establece el valor del pin en 0 (bajo) para apagar el LED.
        """
        self.led.value(0)