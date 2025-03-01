class Identity:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"My name is {self.name} and I am {self.age}")


Shahzaib = Identity("Shahzaib", 19)

Shahzaib.getInfo()