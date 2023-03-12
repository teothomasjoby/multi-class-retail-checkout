import os

def delete_files(path, n=84):
    fileNames = os.listdir(path)
    for fname in fileNames[n:]:
        os.remove(f"{path}/{fname}")

def main():
    for i in range(1,117):
        loc = f"/Users/wolf/Downloads/AIC23_Track4_Automated_Checkout/{i}"
        if os.path.isdir(loc):
            delete_files(loc, 84)


if __name__== "__main__":
    main()
    print("done!")
