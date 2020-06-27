
import os
path = "/home/hekun/mydata/tlt-2.0/examples/ssd/data/train/images/"
labels = "/home/hekun/mydata/tlt-2.0/examples/ssd/data/train/labels/"
files = os.listdir(path)#获取当前目录下的文件
count = 0
for filename in files:
    portion = os.path.splitext(filename)#将文件名拆成名字和后缀
    txtfilename = portion[0]+".txt"
    if portion[1] != ".JPEG":
    	print(portion[0])
    if not os.path.exists(os.path.join(labels,txtfilename)):
    	print(os.path.join(labels,txtfilename))
    	count = count +1
print(count)
    #if portion[1] == ".jpg":#关于后缀
    #    newname = portion[0] + ".JPEG"
    #    os.rename(os.path.join(path, filename), os.path.join(path, newname))