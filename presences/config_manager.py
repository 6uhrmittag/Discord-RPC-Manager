from rpc_tool.main import DiscordRPC, ProcessChecker
import time
from typing import List, Optional


class PresenceConfig:
    def __init__(
        self,
        process_name: str,
        state_running: str,
        details_running: str,
        state_not_running: str,
        details_not_running: str,
        large_image_key: Optional[str] = None,
        large_image_text: Optional[str] = None,
    ):
        self.process_name = process_name
        self.state_running = state_running
        self.details_running = details_running
        self.state_not_running = state_not_running
        self.details_not_running = details_not_running
        self.large_image_key = large_image_key
        self.large_image_text = large_image_text


class PresenceManager:
    def __init__(
        self, client_id: str, configs: List[PresenceConfig], check_interval: int = 5
    ):
        self.rpc = DiscordRPC(client_id)
        self.configs = configs
        self.check_interval = check_interval

    def run(self):
        try:
            while True:
                any_active = False
                for config in self.configs:
                    if ProcessChecker.is_process_running(config.process_name):
                        self.rpc.update_presence(
                            state=config.state_running,
                            details=config.details_running,
                            large_image_key=config.large_image_key,
                            large_image_text=config.large_image_text,
                        )
                        any_active = True
                        break
                if not any_active:
                    self.rpc.reset_presence()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.rpc.close()
