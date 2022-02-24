weight=float(input('Enter your Weight(Kg):'))
height=float(input('Enter your height(m):'))
BMI=weight/(height*height)
print('your BMI is {r:1.3f}'.format(r=BMI))
if BMI<=18.5:
    print('Underweight')
elif BMI>18.5 and BMI<=24.9:
    print('Normal')
elif BMI>25 and BMI<=29.9:
    print('Overweight')
elif BMI>30:
    print('Obese')