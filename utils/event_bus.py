from utils.logger import logger
import collections

class EventBus:
    def __init__(self):
        self.listeners = collections.defaultdict(list)

    def subscribe(self, event_type: str, listener):
        self.listeners[event_type].append(listener)

    def publish(self, event_type: str, data: dict):
        logger.info(f"Olay Yayınlandı: {event_type}")
        for listener in self.listeners[event_type]:
            listener(data)
