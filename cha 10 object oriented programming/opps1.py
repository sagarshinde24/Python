




class Armyform:
    formtype = "Armyform"

    def printData(self):
        print(f"Name is {self.name}")
        
        print(f"Place is {self.place}")


sagarApplication = Armyform()
sagarApplication.name = "sagar"
sagarApplication.place ="pune"
sagarApplication.printData()

#####################################################################################

class ABC():

    def __init__(Self,val):
          print("In class method......")

          Self.val = val
          print("the valu is : ",val)

object= ABC (10)


