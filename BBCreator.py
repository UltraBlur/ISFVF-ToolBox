import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def create_image(row, font_path):
    if row[7] == 'Flat':
        img_size = (1998, 1080)
    elif row[7] == 'Scope':
        img_size = (2048, 858)
    else:
        img_size = (1998, 858)
        
    image = Image.new('RGB', img_size, color = 'black')
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path,40)
    
    # Building a list of lines from columns 2-7
    lines = [str(l) for l in row[1:7]]
    
    for i, line in enumerate(lines, start=0):
        # Calculate width and height of the line
        (line_width, line_height) = (font.getlength(line), 70)
        
        # Calculate x and y coordinates for the centered text
        x = (img_size[0] - line_width) / 2
        y = ((img_size[1] - len(lines)*line_height) / 2) + (i*line_height)
        
        # Drawing a line of text
        d.text((x, y), line, font=font, fill=(255, 255, 255))

    return image

def generate_text_images(csv_path, font_path):
    data = pd.read_csv(csv_path)
    for index, row in data.iterrows():
        directory = row[0] + '_BB.png'
        if not os.path.exists(directory):
            os.makedirs(directory)
        image = create_image(row, font_path)
        image.save(os.path.join(out_path, directory))


# 用您的真实路径替换以下路径
csv_path = "/Users/gaohuyuchen/Desktop/22ISFVF/BB生成脚本/BB脚本自动化.csv"
font_path = "/Users/gaohuyuchen/Desktop/22ISFVF/BB生成脚本/可口可乐在乎体_文本细.ttf"
out_path = "/Volumes/GH_T5_500/BB"
generate_text_images(csv_path, font_path)