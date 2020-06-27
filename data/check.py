import os
path1 = "/home/hekun/mydata/tlt-2.0/examples/ssd/data/train/images/"

for i, filename in enumerate(os.listdir('images')):
    with open(os.path.join(path1,filename), 'rb') as imageFile:
        if imageFile.read().startswith(b'BM'):
            print(f"{i}: {filename} - found!")
        #print("***")