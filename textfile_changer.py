

file_path='/Users/wolf/Downloads/AIC23_Track4_Automated_Checkout/label.txt'
fp=open(file_path,'r')
f=fp.read()
for i in f.split('\n'):
    class_name=i.split(',')[0]
    class_no=i.split(',')[1]
    # print(class_name,class_no)
    # class_name,class_no=i.split(',')
    print(f'{class_no}: {class_name}')
    # print(i)

# print(f)
