class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
indices = []

while True:
    curr_line = input().split()

    if curr_line[0] == 'Stop':
        break

    sender, receiver, content = curr_line

    email = Email(sender, receiver, content)

    emails.append(email)

indices = [int(x) for x in input().split(', ')]

for index in indices:
    emails[index].send()

for element in emails:
    print(element.get_info())

