import utime
from controladorLed import ControladorLed
from controladorSensor import ControladorSensor
from controladorOled import ControladorOled

UMBRAL_POCA_LUZ = 2000

def main():
    print("Programa de control de luz iniciado")
    
    led_delasota = ControladorLed(11)
    sensor_de_nivel_luz_schiaretti = ControladorSensor(14)
    pantalla_oled = ControladorOled(5, 4)
    
    estado_led = False 
    
    while True:
        try:
            utime.sleep(0.5)
            valor_sensor = sensor_de_nivel_luz_schiaretti.mostrar_valor_actual()
            
            if valor_sensor < UMBRAL_POCA_LUZ and not estado_led:
                pantalla_oled.limpiar_pantalla()
                pantalla_oled.escribir_texto('La luz se', 0, 0)
                pantalla_oled.escribir_texto('encendio', 0, 10)
                print('Hay poca luz, se prenderá el led!')
                led_delasota.enciende_led()
                estado_led = True
            elif valor_sensor >= UMBRAL_POCA_LUZ and estado_led:
                pantalla_oled.limpiar_pantalla()
                pantalla_oled.escribir_texto('La luz se', 0, 0)
                pantalla_oled.escribir_texto('apago', 0, 10)
                print('Ya hay suficiente luz, se apagará el led!')
                led_delasota.apagar_led()
                estado_led = False
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()