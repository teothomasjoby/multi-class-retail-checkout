import os
import shutil
path = "/Users/wolf/Downloads/AIC23_Track4_Automated_Checkout/train"
for i in range(119):
    outpath = "/Users/wolf/Downloads/AIC23_Track4_Automated_Checkout/{}".format(i)
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    else:
        shutil.rmtree(outpath)
        os.mkdir(outpath)

    for f in os.listdir(path):
        f2, ext = os.path.splitext(f)
        if i<10:
            if f2.startswith("0000{}".format(i)):
                shutil.copyfile(os.path.join(path, f), os.path.join(outpath, f))
        elif (i>10 and i<100):
            if f2.startswith("000{}".format(i)):
                shutil.copyfile(os.path.join(path, f), os.path.join(outpath, f))
        elif i>100:
            if f2.startswith("00{}".format(i)):
                shutil.copyfile(os.path.join(path, f), os.path.join(outpath, f))


        