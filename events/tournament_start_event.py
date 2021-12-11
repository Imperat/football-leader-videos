import events.constants as constants
from events.basic_event import BasicEvent


class TournamentStartEvent(BasicEvent):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_type(self):
        return constants.TOURNAMENT_START

    def get_duration(self, all_events):
        pass
        # найти окончание турнира
