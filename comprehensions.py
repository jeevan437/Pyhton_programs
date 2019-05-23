
# [<variable>/<expression> for clause <optional condition>]
# list comprehension
print([i for i in range(10) if i%2==0])

# dictionary comprehension
print({i:i*3 for i in range(10)})

l=["hello","python","web services","ruby-on-rails","java"]
print({i:len(i) for i in l if len(i)>4})

#set comprehension
print({i for i in range(10) if i%2==0})