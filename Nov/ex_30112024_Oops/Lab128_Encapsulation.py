class Car:
    def __init__(self,o_name,o_model,o_make):
        self.name=o_name
        self.model=o_model
        self.make=o_make

    def start_engine(self):
        print("Starting the car with the name " +self.name)
        print("Starting the car with the model "+self.model)
        print("Starting the car with the make " + self.make)
lambo=Car("Lambo","V6", "2023")
mg_hector=Car("Hector","1.5 Turbo","2024")
lambo.start_engine()
print("****************")
mg_hector.start_engine()