

#mark = (1,22,6,4)
#percentage = (sum(mark)/400)*100
#print(percentage)


######

def percentage(mark):
    p =((mark[0]+ mark[1]+ mark[2]+ mark[3])/400)*100 
    return p
    
mark1 = (1,22,6,4)
percentage1 = percentage(mark1)


mark2 = (11,12,13,5)
percentage2 = percentage(mark2)
  
print(percentage1,percentage2)

###########

def greet(name):
    print("good day,"+ name)

greet("sagar")

def mysum(num1,num2):
    return num1 + num2

greet("sagar")

s = mysum(10,10)

print(s)

