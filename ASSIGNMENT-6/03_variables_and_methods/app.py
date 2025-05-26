class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

if __name__ == "__main__":
    car1 = Car("Toyota")
    print(car1.brand)
    car1.start()