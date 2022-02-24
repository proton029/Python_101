"""
A company decided to give bonus of 5% to employee if his/her year of service
is more than 5 years.
Ask user for their salary and year of service
and print the net bonus amount.
"""
yearsOfService=int(input('enter years of service:'))
presentSalary=float(input('enter your salary'))
if(yearsOfService>5):
    presentSalary=presentSalary+0.05*presentSalary
    print(presentSalary)
else:
    print('Low expreience')