Age = int(input('Enter your age : ')) 
Gender = input('Select M for male or F for female : ')
if Age<18 and Gender=='M' :
    print('Son')
elif Age<18 and Gender=='F' :
    print('Girl')
elif Age>=18 and Age<=65 and Gender=='M' :
    print('Father')
elif Age>=18 and Age<=65 and Gender=='F' :
    print('Mother')
elif Age>65 and Gender=='M' :
    print('Grandpa')
elif Age>65 and Gender=='F' :
    print('Grandma')
    

