from moviepy.editor import *


def timing_crop(video, parse, turn, w_start_time):
    time_turns = [0, 0]
    b_start_time = (int(parse['time_b'][0]) - int(parse['time_w'][0])) / 1000 + w_start_time
    w_time_in_sec = (int(parse['time_w'][turn - 1]) - int(parse['time_w'][0])) / 1000 + w_start_time
    b_time_in_sec = (int(parse['time_b'][turn - 1]) - int(parse['time_b'][0])) / 1000 + b_start_time
    time_turns[0] = w_time_in_sec - 10
    time_turns[1] = b_time_in_sec + 10
    videoclip = VideoFileClip(video).rotate(90).resize((1920, 1080))
    videoclip = videoclip.subclip(time_turns[0], time_turns[1])
    #     video.write_videofile(filename = str(np.random.randint(10))+video, audio = False)
    return videoclip, w_time_in_sec, b_time_in_sec, time_turns


def speed_clips(videoclip, w_time_in_sec, b_time_in_sec, time_turns, i):
    cliptime = time_turns[1] - time_turns[0]
    sleep = videoclip.subclip(15, cliptime - 12.5)
    start = videoclip.subclip(0, 15)
    end = videoclip.subclip(cliptime - 12.5, cliptime)
    if ((time_turns[1] - 10 - time_turns[0] + 10) > 30):
        sleep = sleep.fx(vfx.speedx, final_duration=10)
        print((time_turns[1] - time_turns[0]) / 10)

    black_wall = VideoFileClip('Black1.jpg').fx(vfx.speedx, final_duration=5)
    table = VideoFileClip(str(i) + '.mp4').resize((1920, 1080))

    #     black_clip = concatenate_videoclips([black_wall, txt_clip], method="compose")
    final = concatenate_videoclips([start, sleep, end, black_wall, table], method="compose")

    final.write_videofile(filename='C:\Users\user\Documents' + str(i) + '.mp4', audio=False)
    return final


def multi_timing_crop(video, timings, turns, start_time, speed):
    i = 1
    videoclips = []
    for turn in turns:
        videoclip, w_time_in_sec, b_time_in_sec, time_turns = timing_crop(video, timings, turn, start_time)
        if speed == 1:
            videoclip = speed_clips(videoclip, w_time_in_sec, b_time_in_sec, time_turns, i)
        videoclips.append(videoclip)
        i += 1
    full_video = concatenate_videoclips(
        [videoclips[0], videoclips[1], videoclips[2], videoclips[3], videoclips[4], videoclips[5], videoclips[6],
         videoclips[7], videoclips[0], videoclips[8], videoclips[9]])
    full_video.write_videofile(filename='C:\Users\user\Documents\fullvideo.mp4', audio=False)
    return 0


multi_timing_crop('Board_3 Vujovic,Ver - Djukic,Sandra 1-0 (1).mp4', pars[2], interesting_turns, 835, 1)
