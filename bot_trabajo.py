import requests
import xml.etree.ElementTree as ET
import time
from deep_translator import GoogleTranslator

# --- CONFIGURACIÓN ---
PHONE = "+1234567890"  # Reemplaza con tu número de teléfono con código de país
API_KEY = "tu_api_key_aqui"  # Reemplaza con tu API Key de CallMeBot

# LIMITE: 10 ofertas por categoria (pero enviadas despacio)
LIMITE_OFERTAS = 10 

FUENTES = {
    "PROGRAMACION": "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "DISENO Y VIDEO": "https://weworkremotely.com/categories/remote-design-jobs.rss",
    "MARKETING": "https://weworkremotely.com/categories/remote-sales-and-marketing-jobs.rss",
    "SOPORTE": "https://weworkremotely.com/categories/remote-customer-support-jobs.rss",
    "OTROS": "https://weworkremotely.com/categories/all-other-remote-jobs.rss"
}

MIS_INTERESES = [
    "Python", "Junior", "Data",
    "Video", "Editor", "Motion", "Graphic", "Adobe", "Designer", "Art",
    "Assistant", "Admin", "Support", "Entry", "Executive", "Manager", "Writer",
    "Spanish", "Español"
]

def traducir_texto(texto_ingles):
    try:
        traductor = GoogleTranslator(source='auto', target='es')
        return traductor.translate(texto_ingles)
    except:
        return texto_ingles

def enviar_whatsapp(categoria, titulo_original, titulo_espanol, link):
    print(f"[INTENTO] Enviando: {titulo_original[:30]}...")
    
    texto = (f"✨ *{categoria}* ✨\n\n"
             f"🇪🇸 *{titulo_espanol}*\n"
             f"(🇺🇸 {titulo_original})\n\n"
             f"🔗 Ver oferta: {link}")
    
    url = f"https://api.callmebot.com/whatsapp.php?phone={PHONE}&text={texto}&apikey={API_KEY}"
    
    try:
        respuesta = requests.get(url, timeout=10)
        
        # VERIFICAMOS SI EL MENSAJE SALIO DE VERDAD
        if respuesta.status_code == 200:
            print("   [OK] Mensaje enviado correctamente.")
            return True
        else:
            print(f"   [ERROR] WhatsApp rechazo el mensaje. Codigo: {respuesta.status_code}")
            print("   (Probablemente estamos enviando muy rapido. Esperando mas...)")
            time.sleep(30) # Castigo: Esperamos 30 segundos si falla
            return False
            
    except Exception as e:
        print(f"   [FALLO] Error de conexion: {e}")
        return False

def buscar_trabajo():
    print(f"--- [BOT 5.0 ANTI-SPAM] Buscando con paciencia... ---")
    
    for nombre_categoria, url_feed in FUENTES.items():
        print(f"\n--> Revisando categoria: {nombre_categoria}...")
        
        try:
            respuesta = requests.get(url_feed)
            root = ET.fromstring(respuesta.content)
            
            encontrados = 0
            
            for item in root.findall('./channel/item'):
                titulo = item.find('title').text
                link = item.find('link').text
                descripcion = item.find('description').text.lower()
                
                for palabra in MIS_INTERESES:
                    if palabra.lower() in titulo.lower() or palabra.lower() in descripcion:
                        
                        titulo_traducido = traducir_texto(titulo)
                        
                        # Intentamos enviar
                        exito = enviar_whatsapp(nombre_categoria, titulo, titulo_traducido, link)
                        
                        if exito:
                            encontrados += 1
                            # PAUSA LARGA: 15 segundos entre mensajes para que no te bloqueen
                            print("   (Esperando 15 segundos para no saturar WhatsApp...)")
                            time.sleep(15) 
                        
                        break 
                
                if encontrados >= LIMITE_OFERTAS:
                    print(f"   (Cupo de {LIMITE_OFERTAS} completado en esta categoria)")
                    break
            
            if encontrados == 0:
                print("   (Nada nuevo por aqui)")

        except Exception as e:
            print(f"Error leyendo la lista {nombre_categoria}: {e}")

    print("\n--- Fin de la busqueda por hoy ---")

if __name__ == "__main__":
    buscar_trabajo()