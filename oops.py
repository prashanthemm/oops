#initiate

class employee:
    #dunder method - constructor
    def __init__(self):
        print("Start")
        self.id = 000
        self.salary = 15000
        self.designation = "SDE"
        print("End")

    def travel(self, destination):
        print("Called")
        print(f"He is traveling to {destination}")

#object
sam =  employee()

#calling method
# print(sam.travel("wallah"))

print(type(sam))