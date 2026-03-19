import subprocess

# URL del canal en vivo
CHANNEL_URL = "https://www.youtube.com/@LaTribu650AM_py/live"

def get_m3u8():
    try:
        # Extrae el link HLS usando yt-dlp
        result = subprocess.check_output(["yt-dlp", "-g", CHANNEL_URL]).decode("utf-8").strip()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

link = get_m3u8()

if link:
    with open("latribu.m3u8", "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXT-X-VERSION:3\n")
        f.write("#EXT-X-STREAM-INF:BANDWIDTH=1280000,RESOLUTION=1280x720\n")
        f.write(link)
    print("Link actualizado con éxito.")
else:
    print("El canal no está en vivo actualmente.")
