class Author:
    authors = {}

    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_author(self, authors):
        authors[self.name] = {}
        authors[self.name]['bio'] = self.biography

    def find_author(self, authors):
        if self.name in authors:
            print(f"{self.name} has been found. Here is some information about them: {authors[self.name]['bio']}")
        else:
            print("Sorry we do not have any information on that author.")

    def show_authors(self, authors):
        for author in authors:
            print(f"{author}: {author['bio']}")

            

