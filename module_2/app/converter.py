import pars

# TODO: import ml & other processing


def get_interesting_moments(pgn_file):
    
    # TODO: pgn ifle analisys & extract interesting moments as Dataframe

    return 0



def convert_video(video_file, pgn_file):
    
    turn = (pgn_file)



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