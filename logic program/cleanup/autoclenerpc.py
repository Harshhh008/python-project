#1.use os module
import os
#2.make files variable and use os.listdir for list of file
files = os.listdir()
#remove autocleanerpc.py file from this program
files.remove("autoclenerpc.py")
#3.print files
print(files)

#4.make function for folder using os.makedirs
def makefolder(folder):
    #if loop for folder exist or not
    if not os.path.exists(folder):
        os.makedirs(folder)


#make function for move files
def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")


makefolder('Images')
makefolder('docs')
makefolder('Media')
makefolder('appications')
makefolder('others')
#5.make imgExts variable for image Extension add more extension for diffrent file

imgExts = [".png",".jpg",".jpeg"]
#6.dicide which file import in which folder
# error : here file extension is upper case than conver lower using lower function
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
print(images)

#for docs
docExts = [".txt",".docx",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
print(docs)

#for media
mediaExts = [".mp3",".mp4",".m4a"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
print(medias)

#for applications
appExts = [".exe"]
apps = [file for file in files if os.path.splitext(file)[1].lower() in appExts]
print(apps)

#for other files
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in imgExts) and (ext not in docExts) and (ext not in appExts) and os.path.splitext(file):
        others.append(file)
print(others)


#call move function
move('Images',images)
move('docs',docs)
move('Media',medias)
move('appications',apps)
move('others',others)






