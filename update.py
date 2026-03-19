import urllib.request
import re

# URL del canal
CHANNEL_URL = "https://www.youtube.com/@LaTribu650AM_py/live"

def get_m3u8():
    try:
        # Simulamos un iPhone para obtener una versión más ligera y directa de la página
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'
        }
        req = urllib.request.Request(CHANNEL_URL, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Buscamos el link m3u8 con una expresión más amplia
            found = re.search(r'(https?://[^\s"<>]+?\.m3u8)', html)
            if found:
                return found.group(1).replace('\\/', '/')
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

link = get_m3u8()

with open("latribu.m3u8", "w") as f:
    f.write("#EXTM3U\n")
    if link:
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:BANDWIDTH=1280000,RESOLUTION=1280x720\n")
        f.write(link + "\n")
    else:
        # Si falla, dejamos el log para saber qué pasó
        f.write("# Canal offline o link no encontrado - Intenta de nuevo en unos minutos\n")

print("Proceso terminado.")
