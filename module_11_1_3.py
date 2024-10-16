from PIL import Image

im = Image.open('gori.jpg')
im_rotate = im.rotate(90)
#im_rotate.save('gori.jpg', quality=95)
#im.close()
im.rotate(45).show()