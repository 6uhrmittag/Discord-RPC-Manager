import pypresence
from typing import Optional


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
