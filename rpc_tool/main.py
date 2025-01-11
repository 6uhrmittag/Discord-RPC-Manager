import sys
import os
import pypresence
import time
from typing import Optional
import psutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DiscordRPC:
    def __init__(self, client_id: str):
        self.rpc = pypresence.Presence(client_id)
        self.rpc.connect()
        self.current_state: Optional[str] = None

    def update_presence(
        self,
        state: str,
        details: str,
        large_image_key: Optional[str] = None,
        large_image_text: Optional[str] = None,
    ):
        if state != self.current_state:
            self.rpc.update(
                state=state,
                details=details,
                large_image=large_image_key,
                large_text=large_image_text,
            )
            self.current_state = state
            print(f"[LOG] Presence updated: {state} - {details}")

    def reset_presence(self):
        if self.current_state is not None:
            self.rpc.clear()
            self.current_state = None
            print("[LOG] Presence reset to default (cleared).")

    def close(self):
        self.rpc.close()


class ProcessChecker:
    @staticmethod
    def is_process_running(process_name: str) -> bool:
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] and process_name.lower() in proc.info["name"].lower():
                return True
        return False


if __name__ == "__main__":
    print("Python executable:", sys.executable)
    print("sys.path:", sys.path)
    print("Current working directory:", os.getcwd())
    client_id = os.getenv("DISCORD_APP_CLIENT_ID")
    if not client_id:
        print("[ERROR] CLIENT_ID not found in environment variables.")
    else:
        print(f"[LOG] Using CLIENT_ID: {client_id}")
