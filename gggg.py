A=int(input("сколько конфет лежит на столе? "))
b=int(input("какое максимальное число конфет будем брать? "))
count=0
while A>0:
    a1=int(input("игрок 1 взял "))
    if a1>b:
        print('вы не честно играете !!!!')
        break
    A1=A-a1    
    if A1 <=0:
        print('1 is winner!!!!')
        break
    else:
        A1=A-a1
        print('на столе осталось ',A1)
    if A1 >= (b*3):
        ab = b
        A2=A1-ab
        print('БОТ взял ',ab)
        print('на столе осталось ',A2)
    else:
        if A1 >= (b*2)+1:
            ab = 1
            A2=A1-ab
            print('БОТ взял ',ab)
            print('на столе осталось ',A2)
        else:
            if A1 >= (b+1):
                ab = A1-(b+1)
                A2=A1-ab
                print('БОТ взял ',ab)
                print('на столе осталось ',A2)
            else:
                if A1 <= b:
                    ab = A1
                    A2=A1-ab
                    print('БОТ взял ',ab)
                    print('на столе осталось ',A2)
                    print('БОТ выиграл!!!!')
                    break
    A=A2