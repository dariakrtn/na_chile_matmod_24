import streamlit as st
from datetime import datetime
from utils import get_sec

import pandas as pd
import random


from converter import create_intersting_clips, create_shots

#st.set_page_config(layout="wide")

#st.markdown(""":rainbow[Interesting Short Generator]""")
st.markdown("""# :rainbow[Interesting Short Generator]""")

# choose file section
col1, col2= st.columns(2)

with col1:
    video_file = st.file_uploader(label="Выберите видео", type=["mp4"])

with col2:
    pgn_file = st.file_uploader(label="Выберите PGN файл", type=["pgn"])


time_str = st.text_input("Введите время первого хода в видео (HH : MM : SS)", "00:00:00")


# choose action section
col1, col2 = st.columns(2)

with col1:
    btn1 = st.button("Создать интерсные моменты")

with col2:
    btn2 = st.button("Создать shots")

# actions
if btn1:

    #check for file presence
    if (video_file != None) and (pgn_file != None):
        
        start_time = get_sec(time_str)
        
        # st.text("Original video")
        # another_video_file = video_file
        # st.video(another_video_file.read())

        # returns arrya of videos in bytes
        videos_bytes, comments = create_intersting_clips(video_file, pgn_file, start_time)
        

        # show video file

        st.subheader("Создание интерсных моментов")

        num_cols = 3
        for i, (video, comment) in enumerate(zip(videos, comments)):
            c = i % num_cols
            if c == 0:
                cols = st.columns(num_cols)
                st.markdown("""---""")
            # cols[c].write(f'{t}')
            # cols[c].image(os.path.join(base_dir, f'camera_rgb_{t}.gif') )
            cols[c].video(video)
            cols[c].markdown(f"""
            #### **Moment {i+1}** 

            Comment: ***{comment}***
            """)

        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

        file_name = date_time

        # download video file
        # st.download_button(label="Download", data=video_file_converted, file_name=file_name)
    else:
        st.error("choose video & pgn")


if btn2:
    
    #check for file presence
    if (video_file != None) and (pgn_file != None):

        start_time = get_sec(time_str)
        
        # st.text("Original video")
        # another_video_file = video_file
        # st.video(another_video_file.read())

        # returns arrya of videos in bytes
        video_bytes = create_shots(video_file, pgn_file, start_time)
        

        # show video file

        st.subheader("Создание Shots")

        # num_cols = 3
        # for i, (video, comment) in enumerate(zip(videos, comments)):
        #     c = i % num_cols
        #     if c == 0:
        #         cols = st.columns(num_cols)
        #         st.markdown("""---""")
        #     # cols[c].write(f'{t}')
        #     # cols[c].image(os.path.join(base_dir, f'camera_rgb_{t}.gif') )
        #     cols[c].video(video)
            
        #     cols[c].markdown(f"""
        #     #### **Shots {i+1}** 

        #     Comment: ***{comment}***
        #     """)
        
        st.video(video_bytes)

        st.markdown(f"""
            #### **Shots** 
            """)

        

        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y-%H-%M-%S")

        file_name = f"{date_time}_shorts.mp4"    

        # download video file
        st.download_button(label="Скачать", data=video_bytes, file_name=file_name)
    else:
        st.error("choose video & pgn file")