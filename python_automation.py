import os
import shutil

path = input("Enter Path: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    # this creates if it does't have  dir
    if not os.path.exists(os.path.join(path, extension)):
     os.makedirs(os.path.join(path, extension))

    # Move the file to the directory corresponding to its extension
shutil.move(os.path.join(path, file), os.path.join(path, extension, file))

print(os.getcwd())
os.chdir("D:\songs")
print(os.getcwd())
