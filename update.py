import subprocess
import os
import re

# ID del canal
CHANNEL_URL = "https://www.youtube.com/@LaTribu650AM_py/live"

def get_m3u8():
    try:
        # Intentamos extraer el link HLS directamente con yt-dlp actualizado
        # Agregamos cookies o headers no son necesarios, pero forzamos el formato
        cmd = ["yt-dlp", "--no-check-certificates", "--quiet", "--no-warnings", "-g", "-f", "best", CHANNEL_URL]
        result = subprocess.check_output(cmd).decode("utf-8").strip()
        if "http" in result:
            return result
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

link = get_m3u8()

# Generamos el archivo siempre para que GitHub Actions no de error
with open("latribu.m3u8", "w") as f:
    f.write("#EXTM3U\n")
    if link and "http" in link:
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:BANDWIDTH=1280000,RESOLUTION=1280x720\n")
        f.write(link + "\n")
    else:
        f.write("# El canal no esta transmitiendo o hubo un error de extraccion\n")

print("Proceso terminado.")
