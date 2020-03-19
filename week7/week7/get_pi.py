import os
import re

# Ved hjælp af re skal du læse filen pi_million_digits 
# og finde ud af hvor mange gange de forskellige cifre er i pi's komma tal

with open('./pi_million_digits.txt') as f:
    addresses = f.read()
p = re.compile(r"(\d{1})")
m = p.findall(addresses)
#print(m)
a = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
for number in a:
    counter = 0
    for i in m:
        if(number == i):
            counter += 1
    print("{} in {}".format(counter, number))