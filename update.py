import urllib.request
import re

CHANNEL_URL = "https://www.youtube.com/@LaTribu650AM_py/live"

def get_m3u8():
    try:
        # Simulamos un navegador real (User-Agent)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        req = urllib.request.Request(CHANNEL_URL, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # Buscamos el link m3u8 en el código fuente
            found = re.search(r'hlsManifestUrl":"(https://.*?\.m3u8)', html)
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
        f.write("# Canal offline o link no encontrado\n")

print("Listo.")
