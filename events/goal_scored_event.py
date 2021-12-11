import events.constants as constants
from events.basic_event import BasicEvent


class GoalScoredEvent(BasicEvent):
    def __init__(self, player_name, team_id):
        super().__init__()
        self.player_name = player_name
        self.team_id = team_id

    def get_type(self):
        return constants.GOAL_SCORED

    def get_duration(self):
        pass
        # следующий гол или 15 секунд.
