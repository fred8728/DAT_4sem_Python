
# Regular expression
# Exercise with search
# In the following text find all the family names of everyone with first name Peter:
# "Peter Hansen was meeting up with Jacob Fransen for a quick lunch, 
# but first he had to go by Peter Beier to pick up some chokolate for his wife. Meanwhile Pastor Peter Jensen 
# was going to church to give his sermon for the same 3 people in his parish. 
# Those were Peter Kold and Henrik Halberg plus a third person who had recently moved here from Norway called Peter Harold".
import re 

txt = """Peter Hansen was meeting up with Jacob Fransen for a quick lunch, but first he had to go by Peter Beier to pick up some chokolate for his wife. Meanwhile Pastor Peter Jensen was going to church to give his sermon for the same 3 people in his parish. Those were Peter Kold and Henrik Halberg plus a third person who had recently moved here from Norway called Peter Harold"""
r'(\d{4})\n(Nykøbing F)'
p = re.compile(r'Peter \w+') #p = pattern
m = p.findall(txt) #match
print(m)