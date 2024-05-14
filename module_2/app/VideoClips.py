import numpy as np
import pandas as pd
from moviepy.editor import *

def timing_crop(videoclip, parse, turn, w_start_time):
    time_turns = [0, 0]
    b_start_time = (int(parse['time_b'][0]) - int(parse['time_w'][0]))/1000 + w_start_time
    w_time_in_sec = (int(parse['time_w'][turn-1]) - int(parse['time_w'][0]))/1000 + w_start_time
    b_time_in_sec = (int(parse['time_b'][turn-1]) - int(parse['time_b'][0]))/1000 + b_start_time
    time_turns[0] = w_time_in_sec - 10
    time_turns[1] = b_time_in_sec + 10
    print(w_time_in_sec, time_turns[0], time_turns[1])
    videoclip = videoclip.rotate(90).subclip(time_turns[0], time_turns[1])
    videoclip.write_videofile(str(np.random.randint(10))+video)
    return videoclip


def multi_timing_crop(videoclip, timings, turns, start_time):
    videoclips = []
    for turn in turns:
        videoclips.append(timing_crop(videoclip, timings, turn, start_time))
    return videoclips