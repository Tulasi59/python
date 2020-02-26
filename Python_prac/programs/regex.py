import re
data  ='''The search() method takes a regular expression pattern and a 
       string and searches for that pattern within the string.
        If the search is successful, search() returns a match object or None otherwise'''

match = re.search('search',data)
print(match) #<_sre.SRE_Match object; span=(4, 10), match='search'>