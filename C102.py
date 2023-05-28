import os
import shutil
#print(dir(os))
#os.mkdir("system")
#os.getcwd()
path=os.listdir("C:/Users/verre/OneDrive/Desktop")
print(path)
path1=os.path.exists("C:/Users/verre/OneDrive/Desktop/abc")
print(path1)
root,ext=os.path.splitext("C:/Users/verre/OneDrive/Desktop/get-pip.py")
print("the root of the file is ",root)
print("the extension of the file is ",ext)


# program to move the files
source="C:/Users/verre/OneDrive/Desktop/abc"
destination="C:/Users/verre/OneDrive/Desktop"

files=os.listdir(source)
for i in files:
    root,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1=source + "/" + i
        path2=destination + "/" + "Image_files"
        path3=destination + "/" + "Image_files" + "/" + i

        if os.path.exists(path2):
            print("Moving " + i + ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + i + ".....")
            shutil.move(path1,path3)

    

      
