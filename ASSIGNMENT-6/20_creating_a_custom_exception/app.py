class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be 18 or above.")

def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid.")

if __name__ == "__main__":
    try:
        check_age(16)
    except InvalidAgeError as e:
        print("Caught an exception:", e)
