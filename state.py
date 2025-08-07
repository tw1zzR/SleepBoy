import asyncio

class BotState:
    def __init__(self):
        self.voice_client = None
        self.sleep_task = None
        self.start_time = None
        self.sleep_time = None
        self.night_mode = False
        self.async_lock = asyncio.Lock()

state = BotState()