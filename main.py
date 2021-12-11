import moviepy.editor as mp
import json

from events.tournament_start_event import TournamentStartEvent
from events.tournament_stopped_event import TournamentStoppedEvent
from events.goal_scored_event import GoalScoredEvent
from events.game_started_event import GameStartedEvent
from events.game_stopped_event import GameStoppedEvent
import events.constants as event_types

video = mp.VideoFileClip("./VID_20211209_193336.mp4")

duration = video.duration


def parse_array_item(item):
    payload = item.get('payload')
    event_type = item.get('description')

    if event_type == event_types.TOURNAMENT_START:
        return TournamentStartEvent(payload.get('name'))

    if event_type == event_types.TOURNAMENT_STOPPED:
        return TournamentStoppedEvent(payload.get('name'))

    if event_type == event_types.GAME_STARTED:
        game_id = payload.get('gameId')
        game_number = payload.get('gameNumber')
        first_team_dict = payload.get('firstTeam')
        second_team_dict = payload.get('secondTeam')

        return GameStartedEvent(game_number, game_id, first_team_dict.get('_id'), first_team_dict.get('name'),
                                second_team_dict.get('_id'), second_team_dict.get('name'))

    if event_type == event_types.GAME_STOPPED:
        game_id = payload.get('gameId')

        return GameStoppedEvent(game_id)

    if event_type == event_types.GOAL_SCORED:
        player_name = payload.get('playerName')
        team_id = payload.get('team_id')

        return GoalScoredEvent(player_name, team_id)


with open('./vso2.json', 'r') as f:
    array = json.load(f)
    # array = list(map(parse_array_item, array))

    events = []
    for (index, item) in enumerate(array):
        event = parse_array_item(item)
        event.set_time(float(item.get('time')))

        events.append(event)

    print('EVENTS', events)

    #final_clip.write_videofile("my_concatenation.mp4")
