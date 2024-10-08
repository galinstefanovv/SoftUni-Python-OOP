class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type_animal: str, sound: str):
        self.name = name
        self.type = type_animal
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"