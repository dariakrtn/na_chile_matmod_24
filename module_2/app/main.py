import streamlit as st
from datetime import datetime
from utils import get_sec

from converter import convert_video

st.set_page_config(layout="wide")

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
    btn1 = st.button("Make interesting video")

with col2:
    btn2 = st.button("Get if game is intersing")

with col3:
    btn3 = st.button("Get interesting moments") 


# actions
if btn1:

    #check for file presence
    if (video_file != None) and (pgn_file != None):

        video_file_converted = convert_video(video_file, pgn_file)
        
        # show video file
        st.video(video_file_converted.read())

        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

        file_name = date_time    

        # download video file
        st.download_button(label="Download", data=video_file_converted, file_name=file_name)
    else:
        st.error("choose video & pgn")


if btn2:
    if (pgn_file != None):
        
        # TODO: check if game is interesting

        st.text("NO")
    
    else:
        st.error("choose pgn file")



if btn3:
    if (pgn_file != None):
        # TODO: choose format for interesting moments
        
        # TODO: get interesting moments

        # TODO: return and show interesting moments
        st.text("some intersgin moments as an array(?) or may be interative table")

    else:
        st.error("choose pgn file")