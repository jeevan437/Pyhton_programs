import re

text = """jeevan kumar
shiva kumar
krishna reddy"""

out =re.split(r'\n+',text)
print(out)

a="hello, welcome !to python"

str = re.split(r', | !',a)
print(str)


num = "8125757360"

phone = re.sub(r'#.+',"",num)
print(phone)