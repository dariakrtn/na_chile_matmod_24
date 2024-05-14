import streamlit as st
from moviepy.editor import VideoFileClip
from io import BytesIO

# get UploadFile

st.file_uploader("load video", ["mp4"], key="video_file")
if "video_file" in st.session_state and st.session_state.video_file:
    
    video_data = st.session_state.video_file.read()

    # print(video_data)

    # Create a BytesIO object to hold the video data
    video_stream = BytesIO(video_data)

    print(video_stream)
    # Load the video from the BytesIO object
    video_clip = VideoFileClip(video_stream)
    # Now you have a VideoClip object called video_clip
    
    new_video_clip = video_clip.cut(5, 10)

    clip.preview(fps = 20)
