import os

#1 takes a path to a folder and writes all filenames in the folder to a specified output file
def write_filenames(folder, output_file):
    with open(output_file, 'w') as File:
        for file in os.listdir(folder):
            File.write(folder + file + '\n')

#2 takes a path to a folder and write all filenames recursively (files of all sub folders to)
#def write_filename_rec(folder, subfolder):

#3 takes a list of filenames and print the first line of each
def print_first_line(filenames):
    for file in filenames:
        with open(file) as File:
                print('Printing first line from file:', File.readlines().pop(0).rstrip())

#4 takes a list of filenames and print each line that contains an email (just look for @)
def print_email(filenames):
    for file in filenames:
        with open(file) as f:
            for line in f:
                if '@' in line:
                    print('Email from list:', line.rstrip())

#5 takes a list of md files and writes all headlines (lines starting with #) to a file 
#Make sure your module can be called both from cli and imported to another module 
#Create a new module that imports utils.py and test each function.

