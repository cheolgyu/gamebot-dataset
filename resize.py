from PIL import Image



image = Image.open('./1.jpg')

resize_image = image.resize((416,416))

resize_image.save('./2.jpg')