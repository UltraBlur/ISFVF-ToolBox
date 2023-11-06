# 对srt帧率进行转换，23.976->24
import re
import datetime

def adjust_timestamps(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()

    new_data = []
    for line in data:
        srt_time_pattern = re.compile("\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")
        result = srt_time_pattern.match(line)
        if result is not None:
            time_range = line.split(' --> ')
            
            start_timestamp = datetime.datetime.strptime(time_range[0], "%H:%M:%S,%f")
            end_timestamp = datetime.datetime.strptime(time_range[1].rstrip(), "%H:%M:%S,%f")

            start_timestamp = start_timestamp + datetime.timedelta(seconds=(start_timestamp.second * 0.001))
            end_timestamp = end_timestamp + datetime.timedelta(seconds=(end_timestamp.second * 0.001))

            line = start_timestamp.strftime("%H:%M:%S,%f")[:-3] + " --> " + end_timestamp.strftime("%H:%M:%S,%f")[:-3] + "\n"
            
        new_data.append(line)


    with open("new_" + file_name, 'w', encoding='utf-8') as f:
        f.writelines(new_data)

input_path = r"Farewell.My.Concubine.1993.1080p.AMZN.WEB-DL.DDP5.1.H.264-Gohan.srt"
adjust_timestamps(input_path)
