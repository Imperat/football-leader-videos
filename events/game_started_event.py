import events.constants as constants
from events.basic_event import BasicEvent


class GameStartedEvent(BasicEvent):
    def __init__(self, game_number, game_id, first_team_id, first_team_name, second_team_id, second_team_name):
        super().__init__()
        self.game_number = game_number
        self.game_id = game_id
        self.first_team_id = first_team_id
        self.first_team_name = first_team_name
        self.second_team_id = second_team_id
        self.second_team_name = second_team_name

    def get_type(self):
        return constants.GAME_STARTED

    def get_duration(self, all_events):
        pass
        # найти окончание игры
