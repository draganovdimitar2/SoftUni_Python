class Customer:
    ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.ID += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = self.ID
