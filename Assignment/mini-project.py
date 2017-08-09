import os

def messages():
    files = os.listdir("/Users/mac/Desktop/alphabet/")
    print(files)
    dir = os.getcwd()
    os.chdir("/Users/mac/Desktop/alphabet/")


    for name in files:
        main = name.translate(None, '0123456789')
        os.rename(name, main)
    os.chdir(dir)
    
messages()
