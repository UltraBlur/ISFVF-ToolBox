import os
import subprocess
import json

def extract_audio(src_folder, dst_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 跳过非视频文件
            if not file.endswith(('.mp4', '.mkv', '.avi', '.mov', '.mxf')):  
                continue
            
            # 计算目标子文件夹的名称和路径
            relative_path = os.path.relpath(root, src_folder)
            dst_subfolder = os.path.join(dst_folder, relative_path)
            os.makedirs(dst_subfolder, exist_ok=True)
            
            # 得到源视频文件的完整路径
            video_path = os.path.join(root, file)

            # 使用ffprobe获取音频信息
            cmd_probe = f'ffprobe -v quiet -print_format json -show_streams -select_streams a "{video_path}"'
            probe_output = subprocess.check_output(cmd_probe, shell=True)
            audio_info = json.loads(probe_output)
            audio_codec = audio_info["streams"][0]["codec_name"]

            # 根据音频编码选择封装格式
            if audio_codec.lower() == "aac":
                audio_extension = ".m4a"
            else:
                audio_extension = ".wav"

            # 得到目标音频文件的完整路径
            audio_path = os.path.join(dst_subfolder, f'{os.path.splitext(file)[0]}{audio_extension}')

            # 使用ffmpeg提取音频
            cmd = f'ffmpeg -i "{video_path}" -map 0:a -c copy -rf64 auto "{audio_path}"'
            subprocess.call(cmd, shell=True)


def extract_aac_audio(src_folder, dst_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 跳过非视频文件
            if not file.endswith(('.mp4', '.mkv', '.avi', '.mov', '.mxf')):  
                continue
            
            # 计算目标子文件夹的名称和路径
            relative_path = os.path.relpath(root, src_folder)
            dst_subfolder = os.path.join(dst_folder, relative_path)
            os.makedirs(dst_subfolder, exist_ok=True)
            
            # 得到源视频文件的完整路径
            video_path = os.path.join(root, file)

            # 使用ffprobe获取音频信息
            cmd_probe = f'ffprobe -v quiet -print_format json -show_streams -select_streams a "{video_path}"'
            probe_output = subprocess.check_output(cmd_probe, shell=True)
            audio_info = json.loads(probe_output)
            audio_codec = audio_info["streams"][0]["codec_name"]

            # 检查音频编码是否为aac
            if audio_codec.lower() == "aac":
                # 得到目标音频文件的完整路径
                audio_path = os.path.join(dst_subfolder, f'{os.path.splitext(file)[0]}.m4a')

                # 使用ffmpeg提取音频
                cmd = f'ffmpeg -i "{video_path}" -map 0:a -c copy "{audio_path}"'
                subprocess.call(cmd, shell=True)
                
# 调用函数处理文件夹。你需要将下面的路径替换为实际情况
extract_audio(r'/Volumes/22ISFVF-NAS/21ISFVF-JSB/01_Original/China', r'/Volumes/22ISFVF-NAS/21ISFVF-JSB/03_Sound/OriginalAudioFiles/China')
#extract_aac_audio(r'/Volumes/22ISFVF-NAS/21ISFVF-JSB/01_Original/Abroad', r'/Volumes/22ISFVF-NAS/21ISFVF-JSB/03_Sound/OriginalAudioFiles/Abroad')