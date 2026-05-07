class Book:

    # Constructor to initialize book details
    def __init__(self,book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed_by = None

    #Method to know the book is borrowed or not
    def borrow(self, memeber_name):
        if self.borrowed_by is not None:
                print(f"Already borrowed by {self.borrowed_by}")

        else:
                self.borrowed_by = memeber_name
                print(f"{self.title} borred by {memeber_name}")

    #To dispplay the status of the book 
    def display_status(self):
        if self.borrowed_by is None:
            print("Available")
        else:
             print(f"Borrowed by {self.borrowed_by}")
    
    #Return the book to make the status to available again
    def return_book(self):
        self.borrowed_by = None
        print(f"{self.title} returned successfully")



b1 = Book("B001", "Wings of Fire", "A.P.J. Abdul Kalam")

b1.display_status()
b1.borrow("Ravi")
b1.display_status()
b1.borrow("Priya")
b1.return_book()
b1.display_status()
