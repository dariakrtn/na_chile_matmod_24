import ffmpeg
from create_audio_comment import audio_comm
from os import remove
from pars import pars_pgn
import json

def cut_video(input_file, output_file, audio_file,  start_time, duration=15, audio_offset=4):
    # Начало и конец обрезки (в секундах)
    # Выполнение обрезки

    video = ffmpeg.input(input_file, ss=start_time, t=duration).filter('transpose', 3)
    audio = ffmpeg.input(audio_file).filter('adelay', f'{audio_offset * 1000}|{audio_offset * 1000}')

    (
        ffmpeg
        .concat(video, audio, v=1, a=1)
        .output(output_file, vcodec='libx264', acodec='aac')
        .run()
    )


def save_clip(video, df, start_time, first_time):
    res = []
    for i in range(len(df)):
        audio_file_i_path = f'data/{i}.wav'
        audio_comm(df['comment'][i], audio_file_i_path)

        if df['color_inter'][i].lower() == 'white':
            st_t = (int(df['time_w'][i]) - int(first_time)) // 1000 + start_time - 5
        else:
            st_t = (int(df['time_b'][i]) - int(first_time)) // 1000 + start_time - 5
        cut_video(video, f'data/clip_{i}.mp4', audio_file_i_path, st_t)
        res.append(f'data/clip_{i}.mp4')
        remove(audio_file_i_path)
    return res


#k = str(open('../Ahackaton/Belgrade2024/Round_1.pgn.pgn').read())
#pars, svg_cadr, frist_t = pars_pgn(k, json.load((open('../Ahackaton/Belgrade2024/Round_1.json', encoding="utf-8"))))
#save_clip('../data/first.mp4', pars[0], 835, frist_t)