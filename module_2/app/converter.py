import pars
import api_promt

# TODO: import ml & other processing


def get_interesting_moments(pgn_file):
    
    # TODO: pgn ifle analisys & extract interesting moments as Dataframe
    pgn_str = pgn_file.read().decode('utf-8')
    print(pgn_str)


    res_json = api_promt.comm_gpt(pgn_str)

    df = pars.pars_pgn(pgn_str, res_json)[0]



    return 0




temp_file_to_save = "../data/videos/tmp_video.mp4"

# func to save BytesIO on a drive
def write_bytesio_to_file(filename, bytesio):
    """
    Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does
    not exist yet. 
    """
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())


def convert_video(video_file, pgn_file, start_time):
    
    pgn_str = pgn_file.read().decode('utf-8')
    print(pgn_str)


    res_json = api_promt.comm_gpt(pgn_str)

    df = pars.pars_pgn(pgn_str, res_json)[0]

    #video_data = video_file
    # video_data = st.session_state.video_file.read()

    #write_bytesio_to_file(temp_file_to_save, video_data)


    # turns = [3, 5, 10] # TODO: generate automaticly
    video_clips = multi_timing_crop(video_file, df, start_time)

    video_file_converted = video_file
    return video_file_converted