
myDict= {
    "pustak":" book",
    "khurchi":"table",
    "pakha":"fan",
    "vastu":"item",
}

print("option are", myDict.keys())

a= input("enter hindi word\n")

print("the meaning of your word is:", myDict[a])


print("the meaning of your word is:", myDict.get(a))



