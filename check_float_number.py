import re 
regex = '[+-]?[0-9]*\.[0-9]*'
floatnum=raw_input("enter the number to check float or not: ")
print bool(re.search(regex, floatnum))






