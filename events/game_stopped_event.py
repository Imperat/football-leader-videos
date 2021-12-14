import events.constants as constants
from events.basic_event import BasicEvent


class GameStoppedEvent(BasicEvent):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id

    def get_type(self):
        return constants.GAME_STOPPED

    def get_duration(self, all_future_events):
        return 3
