class Animals:
    def __init__(self):
        self.name = ''
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = 0
        self.type_of_join = ''
        self.type_of_voice = ''
        self.type_of_corn = ''


    def feed(self):
        return f'{self.name} is fed'

    def get_join(self):
        return f'Some {self.type_of_join}'

    def voice(self):
        return f'Say {self.type_of_voice}'
    def to_string(self):
        return f'''{self.kind_of_animal.title()} 
        Name is: {self.name} 
        Join: {self.type_of_join}
        Voice: {self.type_of_voice} 
        Corn: {self.type_of_corn}
        '''
# animal = Animals()
# print(animal.to_string())

class Goose(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = weight
        self.type_of_join = 'eggs'
        self.type_of_voice = 'krya'
        self.type_of_corn = 'grass'

class Cow(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = weight
        self.type_of_join = 'milk'
        self.type_of_voice = 'Moooo'
        self.type_of_corn = 'grass'

class Sheep(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = weight
        self.type_of_join = 'wool'
        self.type_of_voice = 'bueee'
        self.type_of_corn = 'grass'

class Hen(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = weight
        self.type_of_join = 'eggs'
        self.type_of_voice = 'kudah'
        self.type_of_corn = 'corn'

class Goat(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = weight
        self.type_of_join = 'milk'
        self.type_of_voice = 'bueeeee'
        self.type_of_corn = 'grass'

class Duck(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.kind_of_animal = str(type(self)).split('.')[1][:-2]
        self.weight = weight
        self.type_of_join = 'eggs'
        self.type_of_voice = 'krya'
        self.type_of_corn = 'grass'




class Main():
    farm = {Goose('Black', 2),
            Goose('White', 1.5),
            Cow('Man`ka', 450),
            Sheep('Barashek', 54),
            Sheep('Kudryaviy', 49),
            Hen('COCO', 2),
            Hen('Kukaryeku', 0.9),
            Goat('Horns', 34),
            Goat('Hooves', 40),
            Duck('Kryakva', 3)
            }
    def farm_sound(self):
        for say in self.farm:
            print(say.voice(), end=' ')

    def max_weight(self):
        max_weight_animal = 'Uncle Joue' # jff
        max_weight = -1
        for animal in self.farm:
            if animal.weight > max_weight:
                max_weight_animal = animal
                max_weight = animal.weight
        return max_weight_animal
    def common_weight(self):
        common_weight = 0
        for animal in self.farm:
            common_weight += animal.weight
        return common_weight




Main().farm_sound()
print(Main().max_weight().to_string())
print(Main().common_weight())
