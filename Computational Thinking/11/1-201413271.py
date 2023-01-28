class PersonalData:
    def __init__(self, name, birthday, tall, weight):
        self.name = name
        self.birthday = birthday
        self.tall = tall
        self.weight = weight

    def change_tall(self, new_tall):
        self.tall = new_tall

    def change_weight(self, new_weight):
        self.weight = new_weight

    def get_bmi(self):
        return self.weight / self.tall ** 2

    def get_tall(self):
        return self.tall

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def get_weight(self):
        return self.weight


print('201413271 김석우')
print()

gomduri = PersonalData('곰두리', 970325, 1.7, 60)
print('{}의 생년월일 = {}'.format(gomduri.get_name(), gomduri.get_birthday()))
print('{}의 신장 = {}, 체중 = {}'.format(gomduri.get_name(), gomduri.get_tall(), gomduri.get_weight()))
print('{}의 BMI = {}'.format(gomduri.get_name(), gomduri.get_bmi()))

# change tall and weight
gomduri.change_tall(1.76)
gomduri.change_weight(61)

print('{}의 신장 = {}, 체중 = {}'.format(gomduri.get_name(), gomduri.get_tall(), gomduri.get_weight()))
print('{}의 BMI = {}'.format(gomduri.get_name(), gomduri.get_bmi()))
