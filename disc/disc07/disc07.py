class MinList:

    def __init__(self) :
        self.items = []
        self.size = 0
    
    def append(self, item):
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        smallest_item = min(self.items)
        self.items.remove(smallest_item)
        self.size -= 1
        return smallest_item

class Email:

    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:

    def __init__(self):
        self.clients = {}
    
    def send(self, email):
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        self.clients[client_name] = client

class Client:

    def __init__(self, server, name):
        self.inbox = []

        self.server = server
        self.name = name
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        self.inbox.append(email)

class Pet():

    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)
    
class Cat(Pet):

    def __init__(self, name, owner, lives = 9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    
    def talk(self):
        print(self.name + " says meow!")
    
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more lives to lose :(")

class NoisyCat(Cat):

    def __init__(self, name, owner, lives = 9):
        Cat.__init__(self, name, owner, lives)
    
    def talk(self):
        Cat.talk(self)
        Cat.talk(self)
    
    def __repr__(self):
        
        return "NoisyCat({}, {})".format(repr(self.name), repr(self.owner))