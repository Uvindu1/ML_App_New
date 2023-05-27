import os
path = "final_symbols_split_ttv/train/"
classes_dir = ['0', '1', '-1', '2', '-2', '3', '-3', '4', '-4', '5', '6', '7', '8', '9'] #total labels

for num_class in classes_dir:
    i = 0
    for filename in os.listdir(f'final_symbols_split_ttv/train/{num_class}'):
        file_dir = f'final_symbols_split_ttv/train/{num_class}/'
        sample = f'final_symbols_split_ttv/train/{num_class}/{filename}'
        my_dest = str(i) + ".png"
        # my_source = path + filename
        my_dest = file_dir + my_dest
        # rename() function will
        # rename all the files
        os.rename(sample, my_dest)
        i += 1
