import os
import PIL

folder_path='/Users/wolf/Downloads/AIC23_Track4_Automated_Checkout/train'


for image_file in os.listdir(folder_path):
    if os.path.isdir(f"{folder_path}/{image_file}"):
        continue
    fname, ext = image_file.split(".")
    class_no=int(fname.split("_")[0])
    fp=open(f'{folder_path}/output/{fname}.txt',"w+")
    fp.write(f'{class_no} .5 .5 1 1')
    fp.close()
    # print(f'{class_no} .5 .5 1 1')
    