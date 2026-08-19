a = input('enter:')
if len(a) == 5 and a[::] == a[::-1] :
    print('this number is a palindromic number')
elif len(a) > 5 and a[::] == a[::-1] :
    print('Please enter a 5-digit number')
elif len(a) < 5 and a[::] == a[::-1] :
    print('Please enter a 5-digit number')
else:
    print('Invalid')
