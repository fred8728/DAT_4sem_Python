
import pandas as pd

# Create a generator function that can take a list of names as parameter and return each name. Get approved unisex names here:
# wget -O unisex_navne.xls https://ast.dk/_namesdb/export/names?format=xls&gendermask=4

names = pd.read_excel('https://ast.dk/_namesdb/export/names?format=xls&gendermask=4')
name_lst = list(names)

def get_names(lst):
    current = 5
    while(current <len (lst)):
        yield lst[current]
        current +=1

for name in get_names(name_lst):
    print(name)