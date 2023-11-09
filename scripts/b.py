from PIL import ImageFont, ImageDraw, Image
import pandas as pd

df = pd.read_excel("cert.xlsx")
image = Image.open("intermediate/1.jpeg")
image.convert("RGB")
 
"""2.083 is the scaling factor from changing
    the DPI in the rasterization step
"""

font = ImageFont.truetype("fonts/vivaldi.ttf", round(40*2.083))
color = (0, 51, 94)
thickness = 2

def generate(name):
    text = name
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(text)
    #Calibration for centering the text
    w = w*(463/144)*2.083
    h = h*(37/11)*2.083
    draw.text((548*2.083 - w/2, 390*2.083), text,fill=color, font=font,align='center', stroke_width=0)
    image.save(f"generated/{name}.pdf")
 

l = list(map(lambda i: df.loc[i]['Names'], range(len(df))))
for i in l:
    generate(i)