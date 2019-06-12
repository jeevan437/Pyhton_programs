import re
#search
string = "cake and cookies"
pattern = 'cake'
out = re.search(pattern,string)
print(out)

# match

seq = "Icecream"
pattern1 = "c"

out1 = re.match(pattern1,seq)
print(out1)
seq2 = "cake"
out2 = re.match(pattern1,seq2)
print(out2.group())

