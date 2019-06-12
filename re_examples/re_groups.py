import re
email = "please contact us at : jeevanpjr@gmail.com,siva123@gmail.com"

# out = re.findall(r'[\w]+\@[\w]+\.[\w]+',email)
out = re.findall(r'[a-zA-Z0-9]*\@[a-z]*\.[a-z]+',email)
print(out)

ip = '10.10.10.10'

# str = re.match(r'[\d]+\.[\d]+\.[\d]+\.[\d]+',ip)
str = re.findall(r'[\d]+\.[\d]+\.[\d]+\.[\d]+',ip)

# print(str.group())
print(str)