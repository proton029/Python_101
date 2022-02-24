'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''
totalClasses=int(input('Total classes:'))
attends=int(input('Number of classes attended:'))
percnt=(attends/totalClasses)*100
if(percnt<75):
    print(" you are not allowed, attendance=",percnt)
else:
    print('You are allowed, Welcome')