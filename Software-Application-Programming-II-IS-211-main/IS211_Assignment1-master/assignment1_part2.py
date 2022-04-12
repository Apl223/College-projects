
class Book:
    author = ""
    title = ""
    def __init__(self, author, title):
      self.author = author
      self.title = title
    
    def display(self):
        print(self.title + ", written by " + self.author)
        
if __name__ == "__main__":
    firstbook = Book("John Steinbeck","Of Mice and Men")
    firstbook.display()
    secondbook = Book("Harper Lee","To Kill a Mockingbird")
    secondbook.display()
