import math
print('Введите номер операции:1.Сложение')
n=int(input())
while n<11:
    if n==1:
        a=float(input())
        b=float(input())
        print(a+b)

    if n==2:
        a=float(input())
        b=float(input())
        print(a-b)
    
    if n==3:
        a=float(input())
        b=float(input())
        print(a*b)

     
    if n==4:
        a=float(input())
        b=float(input())
        while b==0:
            print('eror')
            b=float(input())
        print(a/b)
        
    if n==5:
        a=float(input())
        b=float(input())
        print(a**b)   

        
    if n==6:
        a=float(input())
        print(a**0.5)   

    if n==7:
        f=1
        a=float(input())
        for i in range(1,a+1):
            f=f*i
        print(f)

    if n==8:
        a=float(input())
        print(math.sin(a))   
        

    if n==9:
        a=float(input())
        print(math.cos(a))   
        

    if n==10:
        a=float(input())
        print(math.tan(a))
    print('Введите номер следующей операции')
    n=int(input())
        
