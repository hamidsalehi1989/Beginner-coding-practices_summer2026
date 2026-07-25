Age = int(input('Enter your age : ')) 
Gender = input('Select M for male or F for female : ') 
if Age<18 :
    if Gender == 'M' :
        print('Son')
    elif Gender == 'F' :
      print('Girl')
    else:
        print('Not valid')
if Age>=18 and Age<=65 :
    if Gender == 'M' :
        print('Mother')
    elif Gender == 'F' :
      print('Father')
    else:
        print('Not valid')
if Age>65 :
    if Gender == 'F' :
        print('Grandma')
    elif Gender == 'M' :
      print('Grandpa')
    else:
        print('Not valid')
