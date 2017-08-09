import os
import random

def rename_files(path):
    files = os.listdir(path)
    me = os.getcwd()
    os.chdir(path)
    #print(files)

   
    for names in files:
        new_file_name = str(random.randint(1,9)) + names
        os.rename(os.path.join(path, names), os.path.join(path, new_file_name))
        
 
    os.chdir(me)

rename_files("/Users/mac/Desktop/alphabet/")
