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

def format_minutes(seconds):
    return str(seconds // 60) + ':' + str(seconds % 60)

with open('./angar.json', 'r') as f:
    array = json.load(f)
    # array = list(map(parse_array_item, array))

    events = []
    for (index, item) in enumerate(array):
        event = parse_array_item(item)
        event.set_time(float(item.get('time')))

        events.append(event)

    main_clip = mp.VideoFileClip('VID_20211213_200207.mp4')

    clips = [main_clip]

    for (index, event) in enumerate(events):
        clip = None

        if event.get_type() == event_types.TOURNAMENT_START:
            clip = mp.TextClip(event.name, fontsize=20, color='red', bg_color='white')
            clip = clip.set_position((980, 25))

        if event.get_type() == event_types.TOURNAMENT_STOPPED:
            clip = mp.TextClip('Конец', fontsize=20, color='blue')

        if event.get_type() == event_types.GAME_STARTED:
            clip = mp.TextClip(event.first_team_name + ' - ' + event.second_team_name + '(#' +  str(event.game_number + 1) + ')', fontsize=25, color='white', bg_color='#0e497c')
            clip = clip.set_position((25, 25))

        if event.get_type() == event_types.GAME_STOPPED:
            clip = mp.TextClip('Матч окончен', fontsize=20, color='blue')

        if event.get_type() == event_types.GOAL_SCORED:
            clip = mp.TextClip(event.player_name, fontsize=20, color='orange', bg_color='#0e497c')
            clip = clip.set_position((25, 75))

        if clip is not None:
            duration = event.get_duration(events[(index + 1):])

            if duration <= 0:
                duration = 5

            print('clip PROCESSING ---- start and end', event.get_type(), format_minutes(event.get_time()), format_minutes(event.get_time() + duration))
            print()
            clip = clip.set_duration(duration)
            clip = clip.set_start(event.get_time())
            clips.append(clip)

    video = mp.CompositeVideoClip(clips).set_duration(60 * 60 * 1.5)

    video.write_videofile("my_concatenation.mp4", fps=30)

# 1280 x 720