import re
url = raw_input("enter the url")
regex='https?://([A-Za-z_0-9.-]+).*'
result = re.findall(regex,url)
print result
