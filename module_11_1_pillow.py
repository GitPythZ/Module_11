import requests
from PIL import Image, ImageDraw

filename = "pillow.jpg"

# Просмотр изображения
with Image.open(filename) as img:
    img.show()

# ООбрезаю картинку и сохраняю её в другом формате
image = Image.open('pillow.jpg')
cropped = image.crop((100, 100, 500, 600))
cropped.save(r'C:\Users\admin\PycharmProjects\pythonEducationProject\Module_11\cropped_pillow.png')

# Поворот изображения и сохранение в другом формате
image = Image.open('pillow.jpg')
rotated = image.rotate(90)
rotated.save('image_rotated.jpg')

# сохранение изображения из интернета
URL = 'https://www.vashmatrass.ru/files/images/ecommerce/bigproduct-155229250382170100.jpeg'
open_url = requests.get(URL, stream=True).raw
image = Image.open(open_url)
image.save('pillow_url.jpg', 'jpeg')

# создание нового изображения (синий параллелограмм)
cube = Image.new(mode="RGBA", size=(400, 500), color='blue')
cube.show()