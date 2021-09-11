import os
    
def move(type,folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i in type:
        os.replace(i,f"{folder}/{i}") 

files=os.listdir()
files.remove("main.py")

imgExt=(".jpg",".png",".jpeg")
txtExt=(".txt",".doc",".docx",".pdf")
cmpExt=(".zip",".rar")
mediaExt=(".mp4",".mp3",".avi")
images=[]
text=[]
cmprsd=[]
media=[]
others=[]
for file in files:
    ext=os.path.splitext(file)[1]
    if ext.lower() in imgExt:
        images.append(file)
    elif ext.lower() in txtExt:
        text.append(file)
    elif ext.lower() in cmpExt:
        cmprsd.append(file)
    elif ext.lower() in mediaExt:
        media.append(file)
    else:
        if os.path.isfile(file):
            others.append(file)
move(text,'Docs')
move(images,'Images')
move(cmprsd,'Compressed')
move(media,'Media')
move(others,'Other')
