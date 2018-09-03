# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 00:06:29 2018

@author: Selina Siak
"""

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        self.rating = 0

#Method to get a user's email address
    def get_email(self):
        return self.email

#Method to change a user's email address            
    def change_email(self, address):
        self.address = address
        new_email = ()
        if self.address != self.email:
            new_email = self.address
            self.email = self.address
            return "{}'s email address has been updated to {}".format(self.name, new_email)
    
#what is printed out for each user    
    def __repr__(self):
        return "User: {}, Email: {}, number of books read: {}".format(self.name, self.email, len(self.books))

#Method to compare users    
    def __eq__(self, other_user):
        self.other_user = other_user
        
    def read_book(self, book, rating):
        self.book = book
        self.rating = rating
        self.books[self.book] = self.rating
        
    def get_average_rating(self, book, rating):
        self.book = book
        self.rating = rating
        total_rating = 0
        for rating in self.books.values():
            total_rating += rating
            average_rating = total_rating/len(self.books)
        return average_rating
        
#define Book Class
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
  
#Method to get book title
    def get_title(self, title):
        return self.title
 
#Method to get book ISBN
#ISBN must be integer only, no special characters
    def get_isbn(self, isbn):
        return self.isbn
 
#Method to change book ISBN      
    def set_isbn(self, new_isbn):
        if new_isbn != self.isbn:
            self.isbn = new_isbn
            print("The ISBN for {} has been updated".format(self.title))
    
    def __repr__(self):
        return "Book: {}, ISBN: {}".format(self.title, self.isbn)

#Method to add book rating  
    def add_rating(self, rating):
        if self.rating >= 0 and self.rating <=4:
            self.ratings.append(self.rating)
        else:
            print("Invalid Rating")
    
#Method to compare books    
    def __eq__(self, other_book):
        self.other_book = other_book
        
    def get_average_rating(self, rating):
        total_rating = 0
        for rating in self.ratings.values():
            total_rating += rating
            average_rating = total_rating/len(self.books)
        return average_rating
        
    def __hash__(self):
        return hash((self.title, self.isbn))
    
class Fiction(Book):
    def __init__(self, title, isbn, author):
        Book.__init__(self, title, isbn)
        self.author = author
            
    def get_author(self, author):
        return self.author
    
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        if self.level == "beginner":
            return "{}, a {} manual on {}".format(self.title, self.level, self.subject)
        else:
            return "{}, an {} manual on {}".format(self.title, self.level, self.subject)
        
class Tome_Rater(User, Book):
    def __init__(self):
        User.__init__(self, name, email)
        Book.__init__(self, title, isbn)
        self.users = {}
        self.books = {}
        
        
    def create_book(title, isbn):
        return Book(title, isbn)
    
    def create_novel(title, isbn, author):
        return Fiction(title, isbn, author)
    
    def create_non_fiction(title, isbn, subject, level):
        return Non_Fiction(title, isbn, subject, level)
 
    def add_user(name, email, user_books= None):
        if user_books == None:
            return User(name, email)
        else:
            for book in user_books:
                Tome_Rater.add_book_to_user(book, email, rating)
            return User(name, email, user_books) 
    
    def add_book_to_user(book, email, rating):
        if rating == ():
            rating == "None"
            for key in self.users.keys(email):
                if email not in self.users:
                    print("No user with email {}!".format(email))
                else:
                    Tome_Rater.read_book(self, book, rating)
                    Tome_Rater.add_rating(self, rating)
                    if book not in self.books:
                        self.books[book] = 1
                        if book in self.books:
                            self.books[book] += 1
 
    def print_catalog():
        for key in self.books:
            print(key)
    
    def print_users():
        for value in self.users:
            print(value)
    
    def most_read_book():
        count = 0
        book = " "
        for key, value in self.books:
            if value > count:
                count = value
                book == key
        return book
    
    def highest_rated_book():
        highest_rating = 0
        highest_rated_book = " "
        for key in self.books:
            if key.get_average_rating() > highest_rating:
                highest_rating = key.get_average_rating()
                highest_rated_book == key
        return highest_rated_book
    
    def most_positive_user():
        highest_rating = 0
        most_positive_user = " "
        for value in self.users:
            if value.get_average_rating() > highest_rating:
                highest_rating = value.get_average_rating()
                most_positive_user == value
        return most_positive_user
       
#Place for code testing
#sophie = User("Sophie", "sstone70@hotmail.com")
#print(sophie)
#print(sophie.change_email("sophie70@gmail.com"))
#print(sophie)

#TWWBTW = Book("The Woman Who Breathed Two Worlds", 9781603939349)
#print(TWWBTW)
#TWWBTW.set_isbn(978150393934)
#print(TWWBTW)
#WtFCTS = Fiction("When the Future Comes Too Soon", 9781542045759, "Selina Siak Chin Yoke")
#print(WtFCTS)
#Alice = Fiction("Alice in Wonderland", 9780007350827, "Lewis Carroll")
#print(Alice)
#Schwager = Non_Fiction("Technical Analysis on Futures", 471020516, "Investing", "advanced")
#print(Schwager)
#sophie.read_book(TWWBTW, 4)
#from TomeRater import *



#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())