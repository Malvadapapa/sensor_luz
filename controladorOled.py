import machine
from ssd1306 import SSD1306_I2C

class ControladorOled:
    def __init__(self, __pin_scl, __pin_sda):
        # Almacenar los números de pin como atributos privados
        self.__pin_scl = __pin_scl
        self.__pin_sda = __pin_sda
        
        # Inicializar la comunicación I2C
        self.__i2c = machine.SoftI2C(scl=machine.Pin(self.__pin_scl), sda=machine.Pin(self.__pin_sda))
        
        # Crear el objeto de la pantalla OLED (128x64 píxeles)
        self.__display = SSD1306_I2C(128, 64, self.__i2c)

    def limpiar_pantalla(self):
        # Llenar la pantalla con píxeles apagados (0)
        self.__display.fill(0)
        # Actualizar la pantalla para mostrar los cambios
        self.__display.show()

    def escribir_texto(self, texto, x, y):
        # Escribir el texto en la posición especificada
        self.__display.text(texto, x, y)
        # Actualizar la pantalla para mostrar el texto
        self.__display.show()