a = input('Enter a sentence : ')
v = ['a','i','o','e','u']
c=0
for i in a:
    if i in v:
        c+=1
print(c)

# Raveshe dovom:

a = input('Enter a sentence : ')
c=0
for i in a:
    if i=='a' or i=='i' or i=='o' or i=='e'\
          or i=='u' :
            c+=1
print(c)


