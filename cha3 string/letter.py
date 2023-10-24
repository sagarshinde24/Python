

print("******** LETTER ********")

letter='''Dear <|NAME|>,
\tYou are very sharp and intelligent,
\tYou are seleted !\n\tHave a great day ahead!
\t\tThank you'''

name= input("entre your name\n")

date= input("enter your date\n")


letter=letter.replace("<|NAME|>",name)

letter=letter.replace("<|DATE|>",date)


print(letter)
