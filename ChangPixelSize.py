import os
from PIL import Image
path = "final_symbols_split_ttv/train/"
classes_dir = ['0', '1', '-1', '2', '-2', '3', '-3', '4', '-4', '5', '6', '7', '8', '9'] #total labels

for num_class in classes_dir:
    for filename in os.listdir(f'final_symbols_split_ttv/train/{num_class}'):
        sample = f'final_symbols_split_ttv/train/{num_class}/{filename}'
        image = Image.open(sample)
        print(image.size)
        new_image = image.resize((28, 28))
        print(new_image.size)
        new_image.save(f'final_symbols_split_ttv/prosses_train/{num_class}/{filename}')














#
#
# for i in range(0,10):
#     image = Image.open(f'{i}.jpg')
#     print(image.format)
#     image.show()
#     new_image = image.resize((28, 28))
#     new_image.show()
#
# # The file format of the source file.
# print(image.format) # Output: JPEG
#
# # The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
# print(image.mode) # Output: RGB
#
# # Image size, in pixels. The size is given as a 2-tuple (width, height).
# print(image.size) # Output: (1920, 1280)
#
# # Colour palette table, if any.
# print(image.palette) # Output: None
#
# image = Image.open('panda.jpg')
# new_image = image.resize((28, 28))
# new_image.show()
#
# print(image.size) # Output: (1920, 1280)
# print(new_image.size) # Output: (400, 400)