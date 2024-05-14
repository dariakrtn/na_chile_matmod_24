import pars
import api_promt

# TODO: import ml & other processing


def get_interesting_moments(pgn_file):
    
    # TODO: pgn ifle analisys & extract interesting moments as Dataframe

    return 0



def convert_video(video_file, pgn_file):
    
    pgn_str = pgn_file.read()
    print(pgn_str)

    res_json = api_promt.comm_gpt(pgn_str)

    turn = pars.pars_pgn(pgn_file.read(), res_json)



    # TODO: video processing
    
    video_data = st.session_state.video_file.read()

    # Create a BytesIO object to hold the video data
    video_stream = BytesIO(video_data)

    # Load the video from the BytesIO object
    video_clip = VideoFileClip(video_stream)
    # Now you have a VideoClip object called video_clip

    turns = [3, 5, 10] # TODO: generate automaticly
    video_clips = multi_timing_crop(video_clip, turns)

    video_file_converted = video_file
    return video_file_converted 