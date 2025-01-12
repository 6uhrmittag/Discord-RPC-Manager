import sys
import os
from dotenv import load_dotenv
from features.set_rpc.discord_rpc import DiscordRPC
from helper.process_checker import ProcessChecker

# Load environment variables from .env file
load_dotenv()


class RPCManager:
    def __init__(self):
        self.client_id = os.getenv("DISCORD_APP_CLIENT_ID")
        if not self.client_id:
            raise ValueError("[ERROR] CLIENT_ID not found in environment variables.")
        self.discord_rpc = DiscordRPC(self.client_id)
        self.process_checker = ProcessChecker()

    def run(self):
        print("Python executable:", sys.executable)
        print("sys.path:", sys.path)
        print("Current working directory:", os.getcwd())
        print(f"[LOG] Using CLIENT_ID: {self.client_id}")
        # Add more feature initializations and run logic here

    def close(self):
        self.discord_rpc.close()


if __name__ == "__main__":
    manager = RPCManager()
    try:
        manager.run()
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        manager.close()
