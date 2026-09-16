import os
from dotenv import load_dotenv

load_dotenv()

IP = "192.168.0.11"
PORT_NEXTCLOUD = os.getenv("PORT_NEXTCLOUD")
PORT_MUSIC = os.getenv("PORT_MUSIC")

NEXTCLOUD_URL = f"http://{IP}:{PORT_NEXTCLOUD}"
MUSIC_URL = f"http://{IP}:{PORT_MUSIC}"