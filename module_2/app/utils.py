def get_sec(time_str):
    h,m,s = map(int, time_str.split(":"))
    return h*3600 + m*60 + s
