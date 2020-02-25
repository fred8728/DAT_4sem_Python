
import os

#1 create a function that can read all names of files in a folder when given the full path to the folder
def get_folder_names(path):
    return os.listdir(path)


print(get_folder_names('Exercise1'))

