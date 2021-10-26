from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import pathlib
import os

# csv data name => data.csv
# certif base name => Certif.png

df = pd.read_csv(".\data.csv")
font = ImageFont.truetype("D:\.DocsD\VsCode\py\CertificateGenerator\Montserrat\Montserrat-ExtraBoldItalic.ttf",60)
certif_base = ".\Certif.png"
csv_component = "Nama Lengkap"
height_inY = 760
font_color_fill  = "#193498"
align_position = "center"

for index,j in df.iterrows():
    img = Image.open(certif_base)
    width, length = img.size
    draw = ImageDraw.Draw(img)
    x, y = draw.textsize(j[csv_component], font= font)
    x = (width - x)/2
    draw.text(xy=(x ,height_inY),text='{}'.format(j[csv_component]),fill=(font_color_fill),font=font, align=align_position)
    img_rgb = img.convert('RGB') # bacause the 'sertif' file is in .png while .png file has RGBA component, *A means Alpha(transparancy)
    img_rgb.save('.\sertif\{}.jpg'.format(j[csv_component]))

print("Done printing, please check your " + '{}{}'.format(pathlib.Path().resolve(), "\sertif") + " directory")