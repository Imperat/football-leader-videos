import events.constants as constants
from events.basic_event import BasicEvent


class GoalScoredEvent(BasicEvent):
    def __init__(self, player_name, team_id):
        super().__init__()
        self.player_name = player_name
        self.team_id = team_id

    def get_type(self):
        return constants.GOAL_SCORED

    def get_duration(self, all_future_events):
        duration = 15

        for event in all_future_events:
            if event.get_type() == constants.GOAL_SCORED:
                duration = event.get_time() - self.get_time()

        return min(duration, 15)
