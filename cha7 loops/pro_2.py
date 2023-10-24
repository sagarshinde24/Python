
num=int(input("enter the number"))

prime= True

for i in range (2,num):
    if(num%i == 0):
        prime=False
        break

if (prime==1):
        print("this num is prime")

else:
    print("this num is composite")



