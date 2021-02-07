from PIL import ImageFont, ImageDraw, Image

def findLen(str): 
    counter = 0
    while str[counter:]: 
        counter += 1
    return counter

#设置需要显示的字体
fontpath = "font/Dengb.ttf"

#读取列表所有数据
list = []
f = open("list.txt",encoding='utf-8')
while True:
    line = f.readline()
    if line:
        list.append(line.strip('\n'))
    else:
        break
f.close()


for i in list:
    if findLen(i) == 1:
        bk_img = Image.open("background.jpg")
        width = bk_img.width
        height = bk_img.height
        font_1 = ImageFont.truetype(fontpath, int(width*0.3813))
        print(i)
        draw = ImageDraw.Draw(bk_img)
        draw.text((width/2-int(width*0.3813)/2, height/2-int(width*0.3813)/2), i, font = font_1, fill = (255, 255, 255))
        bk_img.save(i+".jpg",dpi=(120,120),quality = 100)
        del bk_img
        del draw
    if findLen(i) == 2:
        bk_img = Image.open("background.jpg")
        width = bk_img.width
        height = bk_img.height
        font_2 = ImageFont.truetype(fontpath, int(width*0.3813))
        print(i)
        draw = ImageDraw.Draw(bk_img)
        draw.text((bk_img.width/2-int(width*0.3813), bk_img.height/2-int(width*0.3813)/2), i, font = font_2, fill = (255, 255, 255))
        bk_img.save(i+".jpg",dpi=(120,120),quality = 100)
        del bk_img
        del draw
    if findLen(i) == 3:
        bk_img = Image.open("background.jpg")
        width = bk_img.width
        height = bk_img.height
        font_3 = ImageFont.truetype(fontpath, int(width*0.3177))
        print(i)
        draw = ImageDraw.Draw(bk_img)
        draw.text((width/2-int(width*0.3177)*1.5, height/2-int(width*0.3177)/2), i, font = font_3, fill = (255, 255, 255))
        bk_img.save(i+".jpg",dpi=(120,120),quality = 100)
        del bk_img
        del draw
    if findLen(i) == 4:
        bk_img = Image.open("background.jpg")
        width = bk_img.width
        height = bk_img.height
        font_4 = ImageFont.truetype(fontpath, int(width*0.2436))
        print(i)
        draw = ImageDraw.Draw(bk_img)
        draw.text((width/2-int(width*0.2436)*2, height/2-int(width*0.2436)/2), i, font = font_4, fill = (255, 255, 255))
        bk_img.save(i+".jpg",dpi=(120,120),quality = 100)
        del bk_img
        del draw
    if findLen(i) == 5:
        bk_img = Image.open("background.jpg")
        width = bk_img.width
        height = bk_img.height
        font_5 = ImageFont.truetype(fontpath, int(width*0.2012))
        print(i)
        draw = ImageDraw.Draw(bk_img)
        draw.text((width/2-int(width*0.2012)*2.5, height/2-int(width*0.2012)/2), i, font = font_5, fill = (255, 255, 255))
        bk_img.save(i+".jpg",dpi=(120,120),quality = 100)
        del bk_img
        del draw
    if findLen(i) == 6:
        bk_img = Image.open("background.jpg")
        width = bk_img.width
        height = bk_img.height
        font_6 = ImageFont.truetype(fontpath, int(width*0.1652))
        print(i)
        draw = ImageDraw.Draw(bk_img)
        draw.text((width/2-int(width*0.1652)*3, height/2-int(width*0.1652)/2), i, font = font_6, fill = (255, 255, 255))
        bk_img.save(i+".jpg",dpi=(120,120),quality = 100)
        del bk_img
        del draw
