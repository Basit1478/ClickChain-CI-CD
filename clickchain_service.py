class ClickChainService:

    def __init__(self, app_name="ClickChain", version="1.0.0"):
        self.app_name = app_name
        self.version = version

    def start(self):
        print(f"[{self.app_name} v{self.version}] Service started successfully.")
        print(f"[{self.app_name}] Listening for events...")

    def get_greeting(self):
        return f"Hello from {self.app_name} v{self.version}!"

    def get_status(self):
        return "RUNNING"
