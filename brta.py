import random

class BRTA:
    def __init__(self) -> None:
        self.__license = {}

    def driving_test(self,email):
        score = random.randint(0,100)
        if score >= 33:
            print("You have passed")
            license_number = random.randint(5000,9999)
            self.__license[email] = license_number
            return license_number
        else:
            print("You failed")
            return False
    
    def validate_licence(self,email,licence):
        for key,val in enumerate(self.__license):
            if key == email and val == licence:
                return True
            else:
                return False