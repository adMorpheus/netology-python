class Animals:
    def __init__(self):
        self._name = ''
        self._kind_of_animal = str(type(self)).split('.')[1][:-2]
        self._weight = 0
        self._type_of_join = ''
        self._type_of_voice = ''
        self._type_of_corn = ''

    def feed(self):
        return f'{self._name} is fed'

    def get_join(self):
        return f'Some {self._type_of_join}'

    def voice(self):
        return f'Say {self._type_of_voice}'

    def __str__(self):
        return f'''{self._kind_of_animal.title()} 
        Name is: {self._name} 
        Join: {self._type_of_join}
        Voice: {self._type_of_voice} 
        Corn: {self._type_of_corn}
        '''


class Poultry(Animals):
    def __init__(self):
        super().__init__()
        self._type_of_join = 'eggs'
        self._type_of_corn = 'corn'


class Livestosk(Animals):
    def __init__(self):
        super().__init__()
        self._type_of_join = 'milk'
        self._type_of_corn = 'grass'




class Goose(Poultry):
    def __init__(self, name, weight):
        super().__init__()
        self._name = name
        self._weight = weight
        self._type_of_voice = 'krya'


class Cow(Livestosk):
    def __init__(self, name, weight):
        super().__init__()
        self._name = name
        self._weight = weight
        self._type_of_voice = 'Moooo'


class Sheep(Livestosk):
    def __init__(self, name, weight):
        super().__init__()
        self._name = name
        self._weight = weight
        self._type_of_join = 'wool'
        self._type_of_voice = 'bueee'


class Hen(Poultry):
    def __init__(self, name, weight):
        super().__init__()
        self._name = name
        self._weight = weight
        self._type_of_voice = 'kudah'


class Goat(Livestosk):
    def __init__(self, name, weight):
        super().__init__()
        self._name = name
        self._weight = weight
        self._type_of_voice = 'bueeeee'


class Duck(Poultry):
    def __init__(self, name, weight):
        super().__init__()
        self._name = name
        self._weight = weight
        self._type_of_voice = 'krya'


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

    def feed_farm(self):
        for animal in self.farm:
            print(f'{animal.feed()} {animal._type_of_corn}')


    def max_weight(self):
        max_weight_animal = 'Uncle Joue'  # jff
        max_weight = -1
        for animal in self.farm:
            if animal._weight > max_weight:
                max_weight_animal = animal
                max_weight = animal._weight
        return max_weight_animal

    def common_weight(self):
        common_weight = 0
        for animal in self.farm:
            common_weight += animal._weight
        return common_weight


Main().farm_sound()
print(Main().max_weight())
Main().feed_farm()
print(Main().common_weight())
