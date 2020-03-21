from PIL import Image, ImageDraw, ImageFont
import os

def wenzishengcheng(title, artist, i):
    img1 = Image.new(mode='RGBA', size=(324, 40), color=(0, 0, 0, 255))
    img2 = Image.new(mode='RGBA', size=(160, 24), color=(0, 0, 0, 255))
    fontpath = os.getcwd() + '/Fonts/udtypos510.ttf'
    font1 = ImageFont.truetype(fontpath, 19)
    font2 = ImageFont.truetype(fontpath, 13)
    drawObj = ImageDraw.Draw(img1)
    drawObj.text([2, 2], title, 'white', font=font1)
    drawObj.text([2, 22], artist, 'white', font=font2)
    img1.save(os.getcwd() + '/output/IDX_ID' + i + '.png')
    drawObj = ImageDraw.Draw(img2)
    drawObj.text([2, 2], '    ' + title, 'white', font=font2)
    img2.save(os.getcwd() + '/output/IDX_MINI_ID' + i + '.png')
