num = int(input("enter number of terms :"))
a = num
num = 0
n1 = 0
n2 = 1
sum = 0
while a >= num :
    num = num + 1
    print(sum)
    n1 = n2
    n2 = sum
    sum = n1 + n2
    


