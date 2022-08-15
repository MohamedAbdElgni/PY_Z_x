from PIL import Image
myImage = Image.open(r'Images\elzero-pillow (1).png')

mY_box = (400, 0, 800, 400)
mY_new_im = myImage.crop(mY_box)
my_con = mY_new_im.convert('L')
my_con.show()
my_haf_d = myImage.crop((0, 400, 1200, 800))
my_haf_d.convert("L").rotate(180).show()
