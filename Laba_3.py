import math
x= int(input("Введите число х: "))
for i in range(1,x+1,2) :
    flag = False
    for k in range(0,int((math.log2(i)))+1) :
        for l in range(0, int(math.log2(i))+1) :
            for m in range(0,int(math.log2(i))+1) :               
                if i==math.pow(3,k)*math.pow(5,l)*math.pow(7,m) :
                    print (i, k, l , m)
                    flag = True
                    break
            if flag :
                break
        if flag : 
            break

