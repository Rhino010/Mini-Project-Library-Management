class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.users = {}
        self.borrowed_books = []

    def add_user(self):
        self.users[self.id] = {}
        self.users[self.id]['name'] = self.name
        self.users[self.id]['borrowed books'] = self.borrowed_books
    
    def view_user_info(self):
        print(f"ID: {self.id}, Name: {self.id['name']}, Books Checked Out: {self.id['borrowed books']}")

    def show_all_users(self):
        for user in self.users.values():
            print(user)
            
