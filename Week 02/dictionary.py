print("====== DATA FOR CAR 1 ======")
car1 = {
    "plateCar1": input("Enter the plate for car 1: "),
    "modelCar1": input("Enter the model for car 1: "),
    "colorCar1": input("Enter the color for car 1: ")
}

print("====== DATA FOR CAR 2 ======")
car2 = {
    "plateCar2": input("Enter the plate for car 2: "),
    "modelCar2": input("Enter the model for car 2: "),
    "colorCar2": input("Enter the color for car 2: ")
}

print("====== DATA FOR CAR 3 ======")
car3 = {
    "plateCar3": input("Enter the plate for car 3: "),
    "modelCar3": input("Enter the model for car 3: "),
    "colorCar3": input("Enter the color for car 3: ")
}

# Dictionary of Cars
carDictionary = {
    "Car #1": car1,
    "Car #2": car2,
    "Car #3": car3
}

print("====== DATA FOR ALL CARS ======")
print(f"{carDictionary}")