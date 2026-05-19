# IA-Python: Proyectos de Estudio y Práctica 🤖

¡Hola! Bienvenido/a a este repositorio.

> **Aviso Importante:** Este proyecto es un **espacio de estudio personal**. El objetivo principal es aprender, mejorar y adquirir nuevos conocimientos en el fascinante mundo de la Inteligencia Artificial y la programación en Python. Por el momento, los proyectos que encontrarás aquí son **réplicas de tutoriales de YouTube** que estoy siguiendo para practicar y entender cómo funciona todo desde cero.

---

## 📂 ¿Qué hay en cada carpeta?

He organizado este repositorio en varias carpetas, cada una con un proyecto o ejercicio distinto. Aquí te explico de forma sencilla (¡sin tecnicismos!) de qué trata cada una:

### 1. Agente de IA 🧠
Aquí encontrarás un pequeño bot conversacional con el que puedes chatear. 
**¡Dato importante!** Todo lo que hay en esta carpeta está construido utilizando las **APIs que Nvidia liberó gratuitamente**. Esto significa que usamos la poderosa tecnología de los servidores de Nvidia para darle "inteligencia" al programa sin tener que pagar por ello.

### 2. Asistente de voz 🎙️
Un programa diseñado para "escuchar" tu voz, entender lo que dices y responderte. Es un ejercicio muy práctico para ver cómo las computadoras pueden comunicarse con nosotros a través de audio.

### 3. RegresionLineal 📈
Este fue un ejercicio para enseñarle a la computadora a hacer "predicciones". Básicamente, le damos datos de la altura y género de varias personas, y el programa aprende a adivinar o estimar cuál debería ser el peso de alguien nuevo.

### 4. Sets de datos 📊
Aquí nos dedicamos a explorar y entender tablas de información (como si fueran hojas de Excel gigantes). El objetivo de esta carpeta es aprender a leer, limpiar y visualizar conjuntos de datos, lo cual es el primer paso antes de crear cualquier Inteligencia Artificial.

---

## 🚀 ¿Cómo usar este repositorio si quieres probarlo?

Si te llama la atención y quieres probar estos proyectos en tu propia computadora, puedes hacerlo siguiendo estos pasos básicos:

### Paso 1: Descargar el proyecto
Primero, descarga estos archivos a tu computadora. Puedes hacerlo descargando el ZIP desde GitHub o usando la terminal:
```bash
git clone https://github.com/TU_USUARIO/IA-Python.git
cd IA-Python
```

### Paso 2: Preparar tu entorno de trabajo
Es muy recomendable crear un "entorno virtual", que es como un cuarto aislado en tu computadora donde instalaremos las herramientas sin afectar nada más.
```bash
# Crear entorno virtual
python -m venv env

# Activar el entorno (en Windows)
env\Scripts\activate
```

### Paso 3: Instalar las herramientas necesarias
Dependiendo de la carpeta a la que entres, necesitarás algunas librerías. Para los proyectos de datos usamos cosas como `pandas` o `scikit-learn`. Para el agente, usamos librerías de IA. Si estás usando el gestor de paquetes `uv`, te facilitará mucho la vida.

### Paso 4: Configurar tus claves secretas (API Keys)
Para que funcionen proyectos como el **Agente de IA** (que se conecta a internet para pensar), necesitarás crear un archivo llamado `.env` dentro de la carpeta correspondiente. Allí deberás pegar tus claves secretas (por ejemplo, la clave gratuita que te da Nvidia al registrarte en su página).

### Paso 5: ¡Ejecutar los programas!
Entra a la carpeta del proyecto que quieras probar y ejecuta su archivo principal. Por ejemplo:
```bash
cd "Agente de IA"
python agente.py
```
*(Si usas uv, puedes correrlo con `uv run agente.py`)*

---
¡Gracias por pasarte por aquí! Espero que estos pequeños proyectos de práctica te sirvan para aprender algo nuevo o te animen a empezar a programar tus propias IAs.
