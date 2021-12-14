import events.constants as constants
from events.basic_event import BasicEvent


class TournamentStartEvent(BasicEvent):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_type(self):
        return constants.TOURNAMENT_START

    def get_duration(self, all_future_events):
        print('------------!', all_future_events)
        for event in all_future_events:
            if event.get_type() == constants.TOURNAMENT_STOPPED:
                return event.get_time() - self.get_time()

        return 0
