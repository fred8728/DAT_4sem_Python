import csv

#A That can print content of a csv file to the console
def print_file_content(file):
    with open(file, newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
            
print_file_content('file1.csv')

#B that can take a list of tuple and write each element to a new line in a file
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as File:
        for item in lst:
            File.write("%s\n" % item)    


list = ("apple", "banana", "cherry")
write_list_to_file('file2.txt', list)

#Ba rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file(output_file, *no):
    with open(output_file, 'w') as File:
        for n in no:
            File.write(n + '\n')  

file = 'file3.txt'
write_list_to_file(file,'chokolade', 'kakao', 'flødeskum')

#C def read_csv(input_file) that take a csv file and read each row into a list
import csv

def read_csv(input_file):
    with open(input_file) as f_obj:
        content = f_obj.readlines()

    for line in content[:10]:
        print(line.strip().split(','))
        
read_csv('befkbhalderstatkode.csv')

