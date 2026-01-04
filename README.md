# DebrScan 🔍🔐

DebrScan es un **pequeño proyecto en Python orientado a ciberseguridad** que permite comprobar si un **puerto TCP está abierto o cerrado** en un host determinado utilizando sockets.

El usuario introduce por consola el **host** (IP o dominio) y el **puerto**, y el script intenta establecer una conexión para determinar su estado.
Este proyecto está pensado como **práctica básica de pentesting y networking**, mostrando cómo funcionan internamente los escaneos de puertos.

---

## 📑 Índice

- [Descripción general 🚀](https://github.com/y9bkh/debrScan/blob/main/README.md#descripción-general-)
- [Tecnologías utilizadas ⚙️](https://github.com/y9bkh/debrScan/blob/main/README.md#tecnolog%C3%ADas-utilizadas-%EF%B8%8F)  
- [Funcionamiento del script 🧠](https://github.com/y9bkh/debrScan/blob/main/README.md#funcionamiento-del-script-)  
- [Instalación y uso 🛠️](https://github.com/y9bkh/debrScan/blob/main/README.md#instalaci%C3%B3n-y-uso-%EF%B8%8F)
- [Ejemplo de ejecución 💡](https://github.com/y9bkh/debrScan/blob/main/README.md#ejemplo-de-ejecuci%C3%B3n-)
- [Aviso legal ⚠️](https://github.com/y9bkh/debrScan/blob/main/README.md#aviso-legal-%EF%B8%8F)
- [Licencia 📖](https://github.com/y9bkh/debrScan/blob/main/README.md#licencia-)  

---

## Descripción general 🚀

DebrScan realiza un **escaneo de puertos TCP básico** utilizando la librería estándar socket de Python.

El script intenta conectarse al puerto especificado:

- Si la conexión se establece correctamente → el puerto está **abierto**
- Si falla o se produce un timeout → el puerto está **cerrado o filtrado**

Este tipo de comprobación es una de las **primeras fases de un proceso de pentesting**, conocida como **enumeración**.

---

## Tecnologías utilizadas ⚙️

- **Python 3** 🐍  
- **socket** (librería estándar de Python para comunicaciones de red TCP/IP)

No se utilizan librerías externas, lo que hace el proyecto ligero y fácil de entender.

---

## Funcionamiento del script 🧠

### 1. Entrada de datos por consola
El script solicita al usuario:

- El **host** a escanear (IP o nombre de dominio)
- El **puerto** a comprobar (entero)

<pre>
  Introduce el host a escanear:
  Introduce el puerto a escanear:
</pre>

### 2. Creación del socket TCP
- Se crea un socket TCP usando AF_INET y SOCK_STREAM
- Se establece un **timeout de 10 segundos** para evitar bloqueos

### 3. Intento de conexión
- El script intenta conectarse al host y puerto indicados
- Si la conexión es exitosa → devuelve `True`
- Si ocurre un error → devuelve `False`

Este comportamiento simula el funcionamiento interno de un port scanner básico.

### 4. Interpretación del resultado
Según el resultado de la conexión:

- Muestra en consola si el puerto está Abierto o Cerrado

---

## Instalación y uso 🛠️
### 1. Clonar el repositorio:
<pre>
  git clone https://github.com/tu_usuario/DebrScan.git
  cd DebrScan
</pre>

### 2. Requisitos
- Python 3 instalado

(No se requieren dependencias adicionales)

### 3. Ejecutar el script:
<pre>
  python debrscan.py
</pre>

---

## Ejemplo de ejecución 💡
Entrada del usuario en consola:
<pre>
  Introduce el host a escanear: 127.0.0.1
  Introduce el puerto a escanear: 80
</pre>

Salida esperada en consola:
<pre>
  Puerto 80 Abierto
</pre>
Si el puerto no está accesible:
<pre>
  Puerto 80 Cerrado
</pre>

---

## Aviso legal ⚠️
Este proyecto se ha desarrollado **exclusivamente con fines educativos.**

⚠️ **No utilices esta herramienta para escanear sistemas, redes o servicios sin autorización explícita.**
El uso indebido de herramientas de escaneo puede ser ilegal.

Utilízala únicamente en:

- Entornos de laboratorio
- Máquinas propias
- Sistemas de pruebas con permiso

---

## Licencia 📖
Este proyecto está bajo la Licencia Pública General de GNU versión 3.0 (GPL-3.0), lo que significa que es software libre. Puedes usar, modificar y distribuir el código, siempre que lo hagas bajo los mismos términos. Para más detalles, consulta el archivo `LICENSE` incluido en este repositorio.
