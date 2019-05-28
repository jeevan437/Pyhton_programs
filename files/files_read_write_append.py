#opening a file from current directory
f = open("employee",'r')
print(f.read())

#opening a file from local machine
f1 = open("E:/Jeevan/test.txt",'r')
print(f1.read())

#writing a file
f2 = open("sample",'w')
f2.write("this is sample file to work with write mode")

# writing a file to lcoal machine
f2= open("E:/Jeevan/test1.txt",'r')
# f2.write("sample file to test with write mode \n adding into a new line")
print(f2.readlines())

f3= open("E:/Jeevan/test2.txt",'a')
f3.write('hello welcome to python')

# f4= open("E:/Jeevan/test3.txt",'w')
# f4.write('[]')