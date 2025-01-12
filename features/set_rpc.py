from helper.config_manager import PresenceConfig, PresenceManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

RPC_SETS = [
    PresenceConfig(
        process_name="Unity Hub.exe",
        state_running="Working on Unity Project",
        details_running="Game Development",
        state_not_running="Unity Not Running",
        details_not_running="Idle",
        large_image_key="unity-logo",
        large_image_text="Unity Engine",
    ),
    PresenceConfig(
       process_name="VirtualDesktop.Streamer.exe",
       state_running="VR",
       details_running="in VR",
       state_not_running="VD Not Running",
       details_not_running="Idle",
       large_image_key="photoshop-logo",
       large_image_text="Adobe Photoshop",
    ),
    PresenceConfig(
        process_name="wsl.exe",
        state_running="using wannabe linux in WSL2",
        details_running="in VR",
        state_not_running="VD Not Running",
        details_not_running="Idle",
        large_image_key="photoshop-logo",
        large_image_text="Adobe Photoshop",
    ),
]

CLIENT_ID = os.getenv("DISCORD_APP_CLIENT_ID")
CHECK_INTERVAL = 5


def main():
    if not CLIENT_ID:
        print("[ERROR] CLIENT_ID not found in environment variables.")
    else:
        print(f"[LOG] Using CLIENT_ID: {CLIENT_ID}")
    manager = PresenceManager(CLIENT_ID, RPC_SETS, CHECK_INTERVAL)
    manager.run()


if __name__ == "__main__":
    main()
