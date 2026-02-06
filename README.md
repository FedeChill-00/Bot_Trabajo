# 🤖 Bot de Alertas de Empleo (Python + WhatsApp)

Este es un bot automatizado que rastrea ofertas de trabajo remoto en **WeWorkRemotely**, las filtra según tus intereses, traduce los títulos al español y te envía una alerta instantánea a **WhatsApp**.

## 🚀 Funcionalidades
* **Scraping RSS:** Lee múltiples fuentes de ofertas (Programación, Diseño, Soporte, etc.).
* **Filtro Inteligente:** Solo notifica si encuentra palabras clave específicas (ej. "Python", "Junior", "Spanish").
* **Traducción Automática:** Usa `deep_translator` para traducir el título de la oferta al español antes de enviarla.
* **Anti-Spam:** Incluye pausas automáticas para evitar bloqueos de la API de WhatsApp.

## 🛠️ Requisitos Previos
1.  Tener **Python 3.x** instalado.
2.  Obtener una API Key gratuita de **CallMeBot** (para enviar mensajes a ti mismo).
    * *Manda un mensaje de WhatsApp al contacto `+34 644 10 55 84` con el texto: `I allow callmebot to send me messages`.*
    * *El bot te responderá con tu API Key.*

## 🔧 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/bot-empleos-whatsapp.git](https://github.com/TU_USUARIO/bot-empleos-whatsapp.git)
    cd bot-empleos-whatsapp
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurar Variables de Entorno:**
    * Crea un archivo llamado `.env` en la carpeta principal.
    * Agrega tus datos (sin espacios):
    ```ini
    WHATSAPP_PHONE=123456789...
    WHATSAPP_API_KEY=123456
    ```
    *(Nota: Reemplaza con tu número real incluyendo el código de país y tu API Key)*.

## ▶️ Uso

Simplemente ejecuta el script principal:

```bash
python bot_trabajo.py
