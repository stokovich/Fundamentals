class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        curr_species = ''
        curr_list_as_string = ''

        if species == 'mammal':
            curr_species = 'Mammals'
            curr_list_as_string = ', '.join(self.mammals)
        elif species == 'fish':
            curr_species = 'Fishes'
            curr_list_as_string = ', '.join(self.fish)
        elif species == 'bird':
            curr_species = 'Birds'
            curr_list_as_string = ', '.join(self.birds)

        return f'{curr_species} in {self.name}: {curr_list_as_string}\nTotal animals: {Zoo.__animals}'


zoo_name = input()
n = int(input())

zoo = Zoo(zoo_name)

for i in range(n):
    curr_line = input().split()
    type_animal = curr_line[0]
    name_animal = curr_line[1]
    zoo.add_animal(type_animal, name_animal)

print(zoo.get_info(input()))
