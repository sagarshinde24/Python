

mark=int(input("enter your mark\n"))

if mark>=90:
    grad="Distingtion"

elif mark>=80:
    grad="A"

elif mark>=70:
    grad="B"

elif mark>=60:
    grad="C"

else:
    grad="F"

print("your grade is: "+ grad)
