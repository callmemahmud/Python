a=input("first number: ")
b=input("second number: ")
c=input("third number:")   #N.B: input takes as string, so we need to type casting.
                           #otherwise,it'll take input but show just the condition which is ' z= (a+b+c)/2 '

a=int(a)
b=int(b)
c=int(c)

z= (a+b+c)/2
print("Avarage: ", z)  #if we devide, it usually shows floating type.
                       #we can check it by " print(type(z))"       