from machine import Pin, ADC

class ControladorSensor:
    def __init__(self, __pinSensor):
        # Almacenar el número de pin como atributo privado
        self.__pinSensor = __pinSensor
        # Configurar la atenuación del ADC a 11dB (rango de voltaje de 0-3.6V)
        self.__adc = ADC.ATTN_11DB
        # Crear un objeto ADC para el pin del sensor
        self.__sensor = ADC(Pin(self.__pinSensor))

    def __configurar_ganancia(self):
        # Método privado para configurar la atenuación del ADC
        self.__sensor.atten(self.__adc)

    def mostrar_valor_actual(self):
        # Configurar la ganancia antes de leer el valor
        self.__configurar_ganancia()
        # Leer el valor actual del sensor
        valor_actual = self.__sensor.read()
        # Devolver el valor leído
        return valor_actual