class Party:
    def __init__(self):
        self.people = []

    def add_person(self, name):
        self.people.append(name)


party = Party()

while True:
    name = input()

    if name == 'End':
        break

    party.add_person(name)

party_as_string = ', '.join(party.people)
print(f'Going: {party_as_string}')
print(f'Total: {len(party.people)}')
