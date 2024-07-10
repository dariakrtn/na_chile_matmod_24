import pars
import api_promt
import VideoClips
from cutting_video import save_clip
import io
import create_audio_comment
import json

from os import listdir, remove
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





def create_intersting_clips(video_file, pgn_file, start_time):

    pgn_str = pgn_file.read().decode('utf-8')

    res_json = api_promt.comm_gpt(pgn_str)
    # with open("./Ahackaton/Belgrade2024/Round_1.json", "r", encoding="utf-8") as f:
    #     res_json = json.loads(f.read())

    df, svg_cadr, first_t = pars.pars_pgn(pgn_str, res_json)
    df = df[0]

    video_data = io.BytesIO(video_file.read())

    video_file_path = "data/video.mp4"
    write_bytesio_to_file(video_file_path, video_data)

    videoClip = save_clip(video_file_path, df, start_time, first_t)
    remove(video_file_path)


    videos_bytes = []
    for i, video_clip in enumerate(videoClip):
        video_file_i_path = f"data/clip_{i}.mp4"
        with open(video_file_i_path, "rb") as f:
            videos_bytes.append(f.read())
        remove(video_file_i_path)
    comments = df["comment"].values

    return videos_bytes, comments




def create_shots(video_file, pgn_file, start_time):
    
    pgn_str = pgn_file.read().decode('utf-8')

    res_json = api_promt.comm_gpt(pgn_str)
   
    df = pars.pars_pgn(pgn_str, res_json)[0][0]

    df = df.loc[df['comment'].notna()]
    df.reset_index(drop=True, inplace=True)
    comments = df["comment"].values

    
    video_data = video_file.read()

    video_file_path = "data/video.mp4"
    write_bytesio_to_file(video_file_path, video_data)
    video = VideoFileClip(video_file_path)
    remove(video_file_path)

    audios = []
    for i, comment in enumerate(comments):
        audio_file_i_path = f"data/audio_file_{i}.wav"
        creat_audio_comment.audio_comm(comment, audio_file_i_path)
        audios.append(AudioFileClip(audio_file_i_path))
        remove(audio_file_i_path)


    video_clip = VideoClips.multi_timing_crop_2(videoClip, df, 1, start_time, audios)


    video_file = "data/video.mp4"
    video_clip.write_videofile(filename=video_file)
    with open(video_file, "rb") as f:
        video_bytes = f.read()
    remove(video_file)




    return video_bytes

