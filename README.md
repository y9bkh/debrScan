# DebrScan 🔍🔐

DebrScan es un **pequeño proyecto en Python orientado a ciberseguridad** que permite comprobar si un **puerto TCP está abierto o cerrado** en un host determinado utilizando sockets.

El usuario introduce por consola el **host** (IP o dominio) y el **puerto**, y el script intenta establecer una conexión para determinar su estado.
Este proyecto está pensado como **práctica básica de pentesting y networking**, mostrando cómo funcionan internamente los escaneos de puertos.

---

## 📑 Índice

- [Descripción general 🚀](https://github.com/y9bkh/AutoWass/blob/main/README.md#descripción-general-)
- [Tecnologías utilizadas ⚙️](https://github.com/y9bkh/AutoWass/blob/main/README.md#tecnolog%C3%ADas-utilizadas-%EF%B8%8F)  
- [Funcionamiento del script 🧠](https://github.com/y9bkh/AutoWass/blob/main/README.md#funcionamiento-del-script-)  
- [Instalación y uso 🛠️](https://github.com/y9bkh/AutoWass/blob/main/README.md#instalaci%C3%B3n-y-uso-%EF%B8%8F)
- [Ejemplo de ejecución 💡](https://github.com/y9bkh/AutoWass/blob/main/README.md#ejemplo-de-ejecuci%C3%B3n-)
- [Licencia 📖](https://github.com/y9bkh/AutoWass/blob/main/README.md#licencia-)  

---

## Descripción general 🚀

DebrScan realiza un escaneo de puertos TCP básico utilizando la librería estándar socket de Python.

El script intenta conectarse al puerto especificado:

- Si la conexión se establece correctamente → el puerto está **abierto**
- Si falla o se produce un timeout → el puerto está **cerrado o filtrado**

Este tipo de comprobación es una de las **primeras fases de un proceso de pentesting**, conocida como **enumeración**.

---

## Tecnologías utilizadas ⚙️

- **Python 3** 🐍  
- **Selenium WebDriver** para automatizar el navegador  
- **Pyperclip** para copiar y pegar texto con emojis y caracteres especiales  
- **Google Chrome** y **ChromeDriver** como navegador y driver de automatización

---

## Funcionamiento del script 🧠

### 1. Entrada de datos por consola
Solicita al usuario:  
- Nombre del contacto  
- Mensaje a enviar  
- Hora de envío en formato HH:MM

### 2. Cálculo del tiempo de espera
- Convierte la hora introducida en un objeto de fecha y hora del día actual  
- Si la hora ya ha pasado, suma un día y programa el envío para el día siguiente  
- Devuelve los segundos totales a esperar usando `datetime` y `timedelta`

### 3. Espera hasta la hora programada
- Muestra en consola el número de segundos que va a esperar  
- Utiliza `time.sleep(segundos)` para pausar la ejecución hasta el momento exacto del envío

### 4. Automatización de WhatsApp Web con Selenium
- Abre Chrome con la opción `detach=True` para mantener el navegador abierto  
- Carga [WhatsApp Web](https://web.whatsapp.com) y pide al usuario que escanee el código QR  
- Busca la barra de búsqueda de chats usando XPath y pega el nombre del contacto con Pyperclip y CTRL + V  
- Entra en el chat del contacto y localiza la caja de escritura  
- Pega el mensaje con Pyperclip y CTRL + V y finalmente lo envía con ENTER

---

## Instalación y uso 🛠️
### 1. Clonar el repositorio:
<pre>git clone https://github.com/y9bkh/AutoWass.git
cd AutoWass</pre>

### 2. Instalar dependencias necesarias:
<pre>pip install selenium pyperclip</pre>

### 3. Configurar ChromeDriver:
* Descarga la versión de ChromeDriver compatible con tu versión de Chrome.​

* Añádelo al PATH del sistema o colócalo en el mismo directorio que el script.

### 4. Ejecutar el script:
<pre>python autowass.py</pre>

### 5. Seguir los pasos en consola:
* Introducir el nombre del contacto exactamente como aparece en WhatsApp.

* Escribir el mensaje que se desea enviar (se permiten emojis y acentos).

* Indicar la hora de envío en formato HH:MM (24h).

* Escanear el QR de WhatsApp Web cuando se abra el navegador y pulsar ENTER cuando esté listo.

---

## Ejemplo de ejecución 💡
Entrada del usuario en consola:
<pre>Introduce el nombre del contacto: Ana Pérez
Introduce el mensaje: ¡Feliz cumpleaños! 🎉🎂
Introduce la hora que desea enviar el mensaje (HH:MM): 09:45
</pre>

Salida esperada en consola:
<pre>Esperando 3600 segundos hasta enviar el mensaje...
Escanea el QR y pulsa ENTER cuando WhatsApp Web esté listo...
</pre>

En segundo plano, el programa:

* Espera el tiempo calculado hasta las 09:45.

* Abre WhatsApp Web, selecciona el chat de Ana Pérez y envía el mensaje automáticamente.

---

## Licencia 📖
Este proyecto está bajo la Licencia Pública General de GNU versión 3.0 (GPL-3.0), lo que significa que es software libre. Puedes usar, modificar y distribuir el código, siempre que lo hagas bajo los mismos términos. Para más detalles, consulta el archivo `LICENSE` incluido en este repositorio.
