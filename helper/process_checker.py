import psutil


class ProcessChecker:
    @staticmethod
    def is_process_running(process_name: str) -> bool:
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] and process_name.lower() in proc.info["name"].lower():
                return True
        return False
