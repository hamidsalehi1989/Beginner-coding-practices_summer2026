w = float(input('enter your weight (KG) :'))
h = float(input('enter your height (M) :'))
BMI = w/(h**2)
if BMI<15:
    print('Malnutriotion')
elif 15<=BMI<16:
    print('Slim')
elif BMI>=16 and BMI<18.5:
    print('Underweight')
elif BMI>=18.5 and BMI<25:
    print('Normal')
elif BMI>=25 and BMI<30:
    print('Overweight')
elif BMI>=30:
    print('Obesity')
