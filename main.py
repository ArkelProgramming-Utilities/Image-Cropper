from PIL import Image
import numpy as np
import math

def cropImage(img_raw, panels=-1, ratio=1):
    width, height = img_raw.size
    print(img_raw.size)
    arr = np.asarray(img_raw)

    if panels == -1:
        panels = math.ceil(width/height/ratio)
        print(panels)

    sideLeng = width/panels
    heightLeng = sideLeng/ratio

    images = []
    for i in range(panels):
        print("img")
        x = arr[math.floor((height-heightLeng)/2):-math.ceil((height-heightLeng)/2), int(i*sideLeng):int((i+1)*sideLeng)]
        images.append(Image.fromarray(x))
    return images

if __name__ == '__main__':
    img = Image.open("img.jpg")
    imgs_out = cropImage(img, ratio=3024/4032)
    for i, img_ in enumerate(imgs_out):
        img_.save("img_{}.jpg".format(i))
