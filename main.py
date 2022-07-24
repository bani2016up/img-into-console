from PIL import Image, ImageDraw 
import PIL

img_path = list(input('Please enter the img path: '))

def replase(replased):
    path = ''
    for i in replased:
        if i == '\\':
            path += '/'
        else:
            path += i
    return path 
   
path = replase(img_path)

print(path)

def get_width_height(img):
    image = Image.open(img) #Открываем изображение. 
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
    width = image.size[0] #Определяем ширину. 
    height = image.size[1] #Определяем высоту. 	
    pix = image.load() #Выгружаем значения пикселей.
    # roteated_img = image.rotate(-90,  PIL.Image.NEAREST, expand = 1).show()
    # rotate_pix = roteated_img.load()

    return width, height, draw, pix, image
    
print(get_width_height(path))

width, height, draw, pix, image, = get_width_height(path)

def mak_duo_chrome(width, height, draw, pix, image):
    factor = 50 #Лемит изменения цвета
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
   
    # image.save('C:/Users/User/Pictures/balckwhite/saeved', "JPEG")
    # del draw
mak_duo_chrome(width, height, draw, pix, image)

def print_img(width, height, pix):
    black = 255*3
    for i in range(width):
        string = ''
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S == black:
                string += '\u25a0'
            else:
                string += '\u25a1'
        print(string)
print_img(width, height, pix)                