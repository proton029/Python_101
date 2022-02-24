print('Doctor Who Festival - Price Calculator\n Note: enter 0 if none')
totalInd=int(input("Enter total number of individuals :"))
u16=int(input("Enter total number of under 16s: "))
fams=int(input("Enter total number of families : "))
print('''Category Price Breakdown:\n 
Price is £204 for 3 individuals\n       
Price is £64.5 for 2 under 16s \n      
Price is £42.75 for 1 families\n
''')
print(f'total persons are {totalInd+u16+(fams*4)}')
print(f'Total Event Price is {(u16*32.5)+(totalInd*68)}\n'
      f'More info and booking visit our website')
