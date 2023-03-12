import json
import os
dir_name = '/Users/wolf/Downloads/AIC23_Track4_Automated_Checkout/labels_1/'
'''read individudual files in labels_1 folder
edit the file and append "Advil Liquid Gel" to prediction
'''
# print(os.cwd())
for fname in os.listdir(dir_name):
    # print(fname+i)
    fp=open(dir_name+fname)
    # print(f)
    data=json.load(fp)
    fp.close()
    data['predictions']=['Advil Liquid Gel']
    # print(json_file)
    with open(dir_name+fname, 'w') as fpw: # 'w' to open for writing
        json.dump(data, fpw)
    
    # json.dump(json_file,f)
    
    

