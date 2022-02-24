# for i in range(10,7,-3):
#     for j in range(10,0,-2):
#         for k in range(8,0,-2):
#             if(k==2):
#                 break
#             else:
#                 print("hi",end=' ')
# for i in range(5):
#     ch=str(i)+' '
#     print(ch*i+' ')

# for i in range(65,91):#ASCII print
#     print(chr(i),end=' ')

# for i in range(1,6):
#     ch=str(i)+' '
#     print(ch*(6-i))
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()
# cnt=0
# for i in range(65,91):
#     print(chr(i),end=' ')
#     cnt+=1
#     if cnt%5==0:
#         print()
for i in range(65,91):
    print((chr(i)+' ')*5)
