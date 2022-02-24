name=input('Enter your name')
for i in name:
    if(i==name[0] or i==name[-1]):
        print(i,end='')
    else:
        print('*',end='')

