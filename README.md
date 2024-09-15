# 🌟 Control de Iluminación Automática

## 👋 Mensaje de Bienvenida

¡Hola! Mi nombre es Cristian Vargas y este es un proyecto para la materia "Aproximación al Mundo del Trabajo" de la Tecnicatura Superior en Desarrollo de Software del ISPC (Instituto Superior Politécnico Córdoba).

## 📌 Descripción General

Este proyecto implementa un sistema de control de iluminación automática utilizando el microcontrolador ESP32 con MicroPython. El sistema monitorea el nivel de luz ambiente y controla un LED en función de la lectura del sensor. Además, muestra información sobre el estado del sistema en una pantalla OLED.

Para ver el código en el simulador: https://wokwi.com/projects/408693301762290689


## 🏗️ Estructura del Programa

#### `main()`

- **Descripción**: Función principal que ejecuta el bucle de control de iluminación.
- **Funcionamiento**:
  1. Inicializa los controladores para LED, sensor y pantalla OLED.
  2. Entra en un bucle infinito que:
     - Lee el valor del sensor de luz.
     - Compara el valor con el umbral y controla el LED en consecuencia.
     - Actualiza la pantalla OLED con el estado actual.


# -----📚 Documentación: ControladorLed -----

## 📌 Descripción General

Este módulo define la clase `ControladorLed`, diseñada para controlar un LED conectado a un pin específico del microcontrolador.

## 🔧 Dependencias

- Módulo `machine` de MicroPython

## 🏗️ Estructura de la Clase

### ControladorLed

#### 🔍 Atributos

- `__pin`: Número del pin al que está conectado el LED (privado)
- `led`: Objeto `Pin` que representa el LED

#### 🛠️ Métodos

##### `__init__(self, pin)`

- **Descripción**: Inicializa el ControladorLed.
- **Parámetros**:
  - `pin` (int): El número del pin al que está conectado el LED.

##### `enciende_led()`

- **Descripción**: Enciende el LED.
- **Funcionamiento**: Establece el valor del pin en 1 (alto).

##### `apagar_led()`

- **Descripción**: Apaga el LED.
- **Funcionamiento**: Establece el valor del pin en 0 (bajo).

## 🚀 Uso

Para utilizar esta clase:

1. Crea una instancia de `ControladorLed` especificando el número de pin.
2. Utiliza los métodos `enciende_led()` y `apagar_led()` para controlar el LED.

### Ejemplo de Código

```python
# Crear una instancia para un LED conectado al pin 2
led_control = ControladorLed(2)

# Encender el LED
led_control.enciende_led()

# Apagar el LED
led_control.apagar_led()





# ----- 📟 Documentación: ControladorOled -----

## 📌 Descripción General

Este módulo define la clase `ControladorOled`, diseñada para controlar una pantalla OLED SSD1306 utilizando el protocolo I2C.

## 🔧 Dependencias

- Módulo `machine` de MicroPython
- Módulo `ssd1306` para controlar la pantalla OLED

## 🏗️ Estructura de la Clase

### ControladorOled

#### 🔍 Atributos

- `__pin_scl`: Número del pin SCL para la comunicación I2C (privado)
- `__pin_sda`: Número del pin SDA para la comunicación I2C (privado)
- `__i2c`: Objeto `SoftI2C` para la comunicación I2C
- `__display`: Objeto `SSD1306_I2C` que representa la pantalla OLED

#### 🛠️ Métodos

##### `limpiar_pantalla()`

- **Descripción**: Limpia la pantalla OLED.
- **Funcionamiento**: Llena la pantalla con píxeles apagados y actualiza la visualización.

##### `escribir_texto(texto, x, y)`

- **Descripción**: Escribe texto en la pantalla OLED en la posición especificada.
- **Parámetros**:
  - `texto` (str): El texto a escribir en la pantalla.
  - `x` (int): La coordenada X donde comenzar a escribir el texto.
  - `y` (int): La coordenada Y donde comenzar a escribir el texto.
- **Funcionamiento**: Escribe el texto en la posición especificada y actualiza la visualización.

## 🚀 Uso

Para utilizar esta clase:

1. Crea una instancia de `ControladorOled` especificando los números de pin para SCL y SDA.
2. Utiliza los métodos `limpiar_pantalla()` y `escribir_texto()` para controlar la pantalla OLED.

### Ejemplo de Código

```python
# Crear una instancia para una pantalla OLED conectada a los pines 22 (SCL) y 21 (SDA)
oled_control = ControladorOled(22, 21)

# Limpiar la pantalla
oled_control.limpiar_pantalla()

# Escribir texto en la pantalla
oled_control.escribir_texto("Hola, Mundo!", 0, 0)




# -----🌡️ Documentación: ControladorSensor -----

## 📌 Descripción General

Este módulo define la clase `ControladorSensor`, diseñada para controlar un sensor analógico utilizando el Convertidor Analógico-Digital (ADC).

## 🔧 Dependencias

- Módulo `machine` de MicroPython (clases `Pin` y `ADC`)

## 🏗️ Estructura de la Clase

### ControladorSensor

#### 🔍 Atributos

- `__pinSensor`: Número del pin al que está conectado el sensor (privado)
- `__adc`: Configuración de atenuación del ADC (privado)
- `__sensor`: Objeto `ADC` que representa el sensor (privado)

#### 🛠️ Métodos

##### `__init__(self, __pinSensor)`
  - `__pinSensor` (int): El número del pin al que está conectado el sensor.

##### `__configurar_ganancia()`

- **Descripción**: Configura la atenuación del ADC (método privado).
- **Funcionamiento**: Establece la atenuación del ADC a 11dB (rango de voltaje de 0-3.6V).

##### `mostrar_valor_actual()`

- **Descripción**: Lee y devuelve el valor actual del sensor.
- **Funcionamiento**: Configura la ganancia y lee el valor del sensor.
- **Retorno**: El valor actual leído del sensor (int).

## 🚀 Uso

Para utilizar esta clase:

1. Crea una instancia de `ControladorSensor` especificando el número de pin al que está conectado el sensor.
2. Utiliza el método `mostrar_valor_actual()` para leer el valor del sensor.

### Ejemplo de Código

```python
# Crear una instancia para un sensor conectado al pin 34
sensor_control = ControladorSensor(34)

# Leer el valor actual del sensor
valor = sensor_control.mostrar_valor_actual()
print(f"Valor del sensor: {valor}")