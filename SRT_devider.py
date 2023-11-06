# 用于简单拆分单个SRT中英文字幕，根据换行拆分，效果maybe欠佳
import re

def extract_subtitles(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()

    chinese_subtitles = []
    english_subtitles = []
    subtitle_id = 1
    for i in range(len(lines)):
        if '-->' in lines[i]:  # This line is a timestamp, subtitles follow
            try:
                chinese_subtitles.append("%s\n%s%s\n" % (subtitle_id, lines[i], lines[i+1]))
                english_subtitles.append("%s\n%s%s\n" % (subtitle_id, lines[i], lines[i+2]))
                subtitle_id += 1
            except IndexError:
                pass

    # Write Chinese subs to a file
    with open('chinese_subtitles.srt', 'w', encoding='utf-8') as f:
        for subtitle in chinese_subtitles:
            f.write("%s" % subtitle)

    # Write English subs to a file
    with open('english_subtitles.srt', 'w', encoding='utf-8') as f:
        for subtitle in english_subtitles:
            f.write("%s" % subtitle)


extract_subtitles('霸王别姬.Farewell.My.Concubine.1993.1080p.GBR.Blu-ray.AVC.LPCM.2.0-Anonymou-4KTY.srt')
