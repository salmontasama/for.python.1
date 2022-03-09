##1##
# num = 0
# for i in range (1,20):
#     num += 1
#     if i %2 !=0:
#      print (i)
##2##
# num1= int(input("enter first number "))
# num2 = int(input("enter second number"))
# for num1 in range (num1,num2):
#     if num1%2 !=0 and num1<num2:
#         print("good",num1,num2)
#3##
# x = int(input("enter '1'or'2'"))
# num1= int(input("enter first number "))
# num2 = int(input("enter second number"))
# for num1 in range (num1,num2):
#     if x == 1 and num1%2 !=0 and num1<num2:
#         print(num1)
#     elif x == 2 and num1%2 ==0 and num1<num2:
#         print(num1)
#     elif  x !=1 and x !=2:
#         print("No suitable number selected")
##5##
# import random
# x = random.randint(1, 1000)
# num = int(input("put number between 1 and 1000"))
# for i in range (1,10):
#     if num ==x:
#         print("Bull's Eye",num,x)
#         break
#     if num <x:
#          print("agine ",num,x)
#          x = random.randint(1, 1000)
#         # print(x)
#          if x != num:
#              y=int(input("this your number?"))
#              if y==1:
#                  continue
#
#     elif num>x:
#          print(num,x)
#          x = random.randint(1, 1000)
#          print(x)
#          if x != num:
#              z = input("this your number?")
#              if z == 1:
#                   continue

##7##
# x = 10
# y = 10
# for i in range(1,y+1):
#     for j in range(1,x+1):
#         print(i * j,"\t",end="")
#     print()