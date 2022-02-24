firstVal=int(input("enter the first celcius val:"))
lastVal=int(input("enter the Last celcius val:"))
print('Celcius\t','Farenheit')
for i in range(firstVal,lastVal+1):
    faren=float(i*(9/5)+32)
    print(i,'\t\t','{r:1.2f}'.format(r=faren))


