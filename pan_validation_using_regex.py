import re
value=raw_input("enter the PAN number: ")
regex="[A-Za-z]{5}\d{4}[A-Za-z]{1}"
print bool(re.match(regex, value))

