import os

classes = ['0', '1', '-1', '2', '-2', '3', '-3', '4', '-4', '5', '6', '7', '8', '9']

# for clss in classes:
#     print('------------' + clss + '-------------')
#
# dirtry = root_dir + '/' + clss
# files = os.listdir(dirtry)
#
# base_outdir = './final_symbols_split_ttv/'
#
# for folder in ['train', 'val', 'test']:
#     target_dir = base_outdir + folder
#     os.makedirs(target_dir + '/' + clss)
#     target_class = target_dir + '/' + clss
#
#     if folder == 'train':
#         images_to_pass = files[: math.floor(0.8*len(files))]
#         for img in images_to_pass:
#             img = dirtry + '/' + img
#             shutil.copy(img, target_class)
#     elif folder == 'val':
#         images_to_pass = files[math.floor(0.8*len(files)): math.floor(0.9*len(files))]
#         for img in images_to_pass:
#             img = dirtry + '/' + img
#             shutil.copy(img, target_class)
#     else:
#         images_to_pass = files[math.floor(0.9*len(files)):]
#         for img in images_to_pass:
#             img = dirtry + '/' + img
#             shutil.copy(img, target_class)

# # Creating Train / Val / Test folders (One time use)
import os
import numpy as np
import shutil
import random
root_dir = './final_symbols_split_ttv/' # data root path
classes_dir = ['0', '1', '-1', '2', '-2', '3', '-3', '4', '-4', '5', '6', '7', '8', '9'] #total labels

val_ratio = 0.15
test_ratio = 0.05

for num_class in classes_dir:
    for filename in os.listdir(f'final_symbols_split_ttv/train/{num_class}'):
        sample = f'final_symbols_split_ttv/train/{num_class}/{filename}'
        print(sample)

# for cls in classes_dir:
#     os.makedirs(root_dir +'train/' + cls)
#     os.makedirs(root_dir +'val/' + cls)
#     os.makedirs(root_dir +'test/' + cls)


# Creating partitions of the data after shuffeling
# src = root_dir + cls # Folder to copy images from
#
# allFileNames = os.listdir(src)
# np.random.shuffle(allFileNames)
# train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
#                                                           [int(len(allFileNames)* (1 - (val_ratio + test_ratio))),
#                                                            int(len(allFileNames)* (1 - test_ratio))])
#
#
# train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
# val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
# test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]
#
# print('Total images: ', len(allFileNames))
# print('Training: ', len(train_FileNames))
# print('Validation: ', len(val_FileNames))
# print('Testing: ', len(test_FileNames))
#
# # Copy-pasting images
# for name in train_FileNames:
#     shutil.copy(name, root_dir +'train/' + cls)
#
# for name in val_FileNames:
#     shutil.copy(name, root_dir +'val/' + cls)
#
# for name in test_FileNames:
#     shutil.copy(name, root_dir +'test/' + cls)