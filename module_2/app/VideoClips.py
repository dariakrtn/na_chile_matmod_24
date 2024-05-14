import numpy as np
import pandas as pd
from moviepy.editor import *
import chess
import chess.pgn
import json
from datetime import datetime

def timing_crop_2(video, parse, turn, w_start_time, audio):
    time_turns = [0, 0]
    audio_clip = AudioFileClip(audio)
    b_start_time = (int(parse['time_b'][0]) - int(parse['time_w'][0]))/1000 + w_start_time
    w_time_in_sec = (int(parse['time_w'][turn-1]) - int(parse['time_w'][0]))/1000 + w_start_time
    b_time_in_sec = (int(parse['time_b'][turn-1]) - int(parse['time_b'][0]))/1000 + b_start_time
    time_turns[0] = w_time_in_sec - 10
    time_turns[1] = b_time_in_sec + 10
    videoclip = VideoFileClip(video).rotate(90).resize((1920, 1080))
    videoclip = videoclip.subclip(time_turns[0], time_turns[1]).set_audio(audio_clip)
    #video.write_videofile(filename = str(np.random.randint(10))+video)
    return videoclip, w_time_in_sec, b_time_in_sec, time_turns



def timing_crop_1(videoclip, parse, turn, w_start_time):
    time_turns = [0, 0]
    b_start_time = (int(parse['time_b'][0]) - int(parse['time_w'][0]))/1000 + w_start_time
    w_time_in_sec = (int(parse['time_w'][turn-1]) - int(parse['time_w'][0]))/1000 + w_start_time
    b_time_in_sec = (int(parse['time_b'][turn-1]) - int(parse['time_b'][0]))/1000 + b_start_time
    time_turns[0] = w_time_in_sec - 10
    time_turns[1] = b_time_in_sec + 10
    print(w_time_in_sec, time_turns[0], time_turns[1])
    videoclip = videoclip.rotate(90).subclip(time_turns[0], time_turns[1])
    #videoclip.write_videofile(str(np.random.randint(10))+video)
    return videoclip



def speed_clips(videoclip, w_time_in_sec, b_time_in_sec, time_turns, i, audio):
    audio_clip = AudioFileClip(audio)
    cliptime = time_turns[1]-time_turns[0]
    sleep = videoclip.subclip(15, cliptime-12.5)
    start = videoclip.subclip(0, 15)
    end = videoclip.subclip(cliptime-12.5, cliptime)
    if ((time_turns[1]-10 - time_turns[0]+10) > 30):
        sleep = sleep.fx(vfx.speedx, final_duration = 10)
        print((time_turns[1] - time_turns[0])/10)
    
    black_wall = VideoFileClip('Black1.jpg').fx(vfx.speedx, final_duration = 5)
    table = VideoFileClip(str(i) +'.mp4').resize((1920, 1080))
    
#     black_clip = concatenate_videoclips([black_wall, txt_clip], method="compose")
    final = concatenate_videoclips([start, sleep, end, black_wall, table], method="compose").set_audio(audio_clip)
    
    #final.write_videofile(filename=f'C:\Users\user\Documents{str(i)}.mp4')
    return final


# creates array of videos
def multi_timing_crop_1(videoclip, timings, start_time):
    
    timings = timings.loc[timings['comment'].notna()]
    timings.reset_index(drop=True, inplace=True)

    # print(timings)
    turns = timings["num_move"].values
    #print(turns)

    videoclips = []
    for turn in turns:
        videoclips.append(timing_crop_1(videoclip, timings, turn, start_time))
    return videoclips

# create 1 shot video
def multi_timing_crop_2(video, timings, start_time, speed, audio):
    
    
    timings = timings.loc[timings['comment'].notna()]
    timings.reset_index(drop=True, inplace=True)

    # print(timings)
    turns = timings["num_move"].values
    #print(turns)

    i = 1
    videoclips = []
    for turn in turns:
        videoclip, w_time_in_sec, b_time_in_sec, time_turns = timing_crop(video, timings, turn, start_time, audio[i])
        if speed == 1:
            videoclip = speed_clips(videoclip, w_time_in_sec, b_time_in_sec, time_turns, i, audio[i])
        videoclips.append(videoclip)
        i+= 1
    full_video = concatenate_videoclips([videoclips[0], videoclips[1], videoclips[2], videoclips[3], videoclips[4], videoclips[5], videoclips[6], videoclips[7], videoclips[0], videoclips[8], videoclips[9]])
    
    return full_video
