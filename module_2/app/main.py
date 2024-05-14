import streamlit as st
from datetime import datetime
from utils import get_sec

import pandas as pd
import random


from converter import create_intersting_clips

#st.set_page_config(layout="wide")

# choose file section
col1, col2= st.columns(2)

with col1:
    video_file = st.file_uploader(label="Choose a video", type=["mp4"])

with col2:
    pgn_file = st.file_uploader(label="Choose a PGN", type=["pgn"])


time_str = st.text_input("Enter time when first move occured (HH : MM : SS)", "00:00:00")


# choose action section
col1, col2, col3 = st.columns(3)

with col1:
    btn1 = st.button("Get interesting moments")

with col2:
    btn2 = st.button("Make shots")


# actions
if btn1:

    #check for file presence
    if (video_file != None) and (pgn_file != None):

        start_time = get_sec(time_str)
        
        # st.text("Original video")
        # another_video_file = video_file
        # st.video(another_video_file.read())

        # returns arrya of videos in bytes
        videos, comments = create_intersting_clips(video_file, pgn_file, start_time)
        

        # show video file

        num_cols = 3
        for i, (video, comment) in enumerate(zip(videos, comments)):
            print(comment)
            c = i % num_cols
            if c == 0:
                cols = st.columns(num_cols)
            # cols[c].write(f'{t}')
            # cols[c].image(os.path.join(base_dir, f'camera_rgb_{t}.gif') )
            cols[c].video(video)
            cols[c].write(comment)

        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

        file_name = date_time    

        # download video file
        #st.download_button(label="Download", data=video_file_converted, file_name=file_name)
    else:
        st.error("choose video & pgn")


if btn2:
    if (video_file != None) and (pgn_file != None):
        # TODO: choose format for interesting moments
        
        # TODO: get interesting moments

        # TODO: return and show interesting moments
        st.text("some intersgin moments as an array")

    else:
        st.error("choose pgn file")