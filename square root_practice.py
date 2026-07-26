Number = float(input('Enter your number : '))
Root = float(input('Enter the root number you want : '))
# P represents power
P = 1/Root
SQRT = Number**P
if Number >= 1 and Root >= 2:
    print('Square root is : ',SQRT)
elif Number < 1 and Root < 2:
    print('Enter the values again ! ')
