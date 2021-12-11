import events.constants as constants
from events.basic_event import BasicEvent


class TournamentStoppedEvent(BasicEvent):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_type(self):
        return constants.TOURNAMENT_STOPPED

    def get_duration(self):
        return 5
