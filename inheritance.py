# class animal:
#     def __init__(self, name):
#         self.name = name 
    
#     def speak(self):
#         print(f"{self.name} makes a sound")

# class dog(animal):
#     def speak(self):
#         print(f"{self.name} barks")



# # abc = animal("Generic")
# # abc.speak()

# ghi = dog("wolfy")
# ghi.speak()

# ----------------------------------------------
# super keyword

class animal:
    def __init__(self):
        self.name = "wolfy" 
    
    def speak(self):
        print(f"{self.name} makes a sound")

class dog(animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is of {self.breed} breed.")




ghi = dog("poodle")
ghi.speak()