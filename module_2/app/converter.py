import pars
import api_promt
import VideoClips
import json

from os import listdir
from os.path import isfile, join


# TODO: import ml & other processing




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



def get_interesting_moments(pgn_file):
    
    # TODO: pgn ifle analisys & extract interesting moments as Dataframe
    pgn_str = pgn_file.read().decode('utf-8')
    print(pgn_str)


    res_json = api_promt.comm_gpt(pgn_str)

    df = pars.pars_pgn(pgn_str, res_json)[0]

    return 





def create_intersting_clips(video_bytes, pgn_str, start_time):
    
    #pgn_str = pgn_file.read().decode('utf-8')
    with open("./Ahackaton/Belgrade2024/Round_1.pgn.pgn", "r", encoding="utf-8") as f:
        pgn_str = f.read()
    #print(pgn_str)

    
    #res_json = api_promt.comm_gpt(pgn_str)
    with open("./Ahackaton/Belgrade2024/Round_1.json", "r", encoding="utf-8") as f:
        res_json = json.loads(f.read())
   
    df = pars.pars_pgn(pgn_str, res_json)[0]

    
    df = df.loc[df['comment'].notna()]
    df.reset_index(drop=True, inplace=True)
    comments = df["comment"].values
    print(comments)

    #video_data = video_file
    # video_data = st.session_state.video_file.read()

    #write_bytesio_to_file(temp_file_to_save, video_data)


    # turns = [3, 5, 10] # TODO: generate automaticly
    # video_clips = VideoClips.multi_timing_crop(video_file, df, start_time)
    # TODO: convert vei_clips to videos in bytes
    
    
    # TEMP
    videos = [] 

    path = "data/videos"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        with open(f"{path}/{file}", "rb") as f:
            videos.append(f.read())
    

    #video_file_converted = video_file
    

    return videos, comments