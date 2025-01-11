from presences.config_manager import PresenceConfig, PresenceManager
import requests
import json
from typing import Optional, List, Dict
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Idle:
    API = "https://discord.com/api/v9"

    class Headers:
        TOKEN = "Authorization"

    class Data:
        SETTINGS = "users/@me/settings"


class Idler:
    def __init__(self, token: str):
        self.token = token
        print(f"[LOG] Idler initialized with token: {token}")

    def change_status(self, status: Dict[str, str]):
        if not status:
            print("[LOG] No status provided to change.")
            return
        url = f"{Idle.API}/{Idle.Data.SETTINGS}"
        headers = {Idle.Headers.TOKEN: self.token}
        payload = {"custom_status": status}
        print(f"[LOG] Changing status to: {payload}")
        try:
            response = requests.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            print(f"[LOG] Status changed successfully: {response.json()}")
            print(f"[LOG] Response status code: {response.status_code}")
            print(f"[LOG] Response headers: {response.headers}")
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to change status: {e}")
            if e.response is not None:
                print(f"[ERROR] Response content: {e.response.content}")
                print(f"[ERROR] Response status code: {e.response.status_code}")
                print(f"[ERROR] Response headers: {e.response.headers}")


class StatusManager:
    def __init__(self, token: str, config_file: str):
        self.idler = Idler(token)
        self.statuses = self.load_statuses(config_file)
        print(
            f"[LOG] StatusManager initialized with token: {token} and config_file: {config_file}"
        )

    def load_statuses(self, config_file: str) -> List[Dict[str, str]]:
        with open(config_file, "r", encoding="utf-8") as file:
            statuses = json.load(file)
            print(f"[LOG] Loaded statuses: {statuses}")
            return statuses

    def update_status(self, status_name: str):
        print(f"[LOG] Updating status to: {status_name}")
        status = next((s for s in self.statuses if s["name"] == status_name), None)
        if status:
            print(f"[LOG] Found status: {status}")
            self.idler.change_status(status["custom_status"])
        else:
            print(f"[ERROR] Status with name '{status_name}' not found.")


if __name__ == "__main__":
    browser_token = os.getenv("DISCORD_BROWSER_TOKEN")
    if not browser_token:
        print("[ERROR] DISCORD_BROWSER_TOKEN not found in environment variables.")
    else:
        print(f"[LOG] Using DISCORD_BROWSER_TOKEN: {browser_token}")
    config_file = os.path.join(os.path.dirname(__file__), "status_config.json")
    manager = StatusManager(browser_token, config_file)
    if len(sys.argv) > 1:
        status_name = sys.argv[1]
    else:
        status_name = "Idle"
    manager.update_status(status_name)
