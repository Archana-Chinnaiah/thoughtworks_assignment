class Book:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
class Author:
    def __init__(self,name,age,nationality,book):
        self.name=name
        self.age=age
        self.nation=nationality
        self.book=book
        
 
def total_price(books):
    total_cost=0
    for i in books:
        total_cost=total_cost+i.price
    return total_cost    

def no_of_books(authors,book_by_author):
    count=0
    for i in authors:
        if(book_by_author==i.name):
            count=count+1
    return count       
        
    
def affortable_books(authors,books):
    affort_books=[]
    for i in books:       
            if i.price<1000:
                affort_books.append(i.name)
    for i in authors:
        for j in affort_books:
            if i.book==j:
                print("\n* The book '",j,"' written by '",i.name,"' is in affortable price")


python=Book('PYTHON',999)
scala=Book('SCALA',1500)
java=Book('JAVA',800)
c=Book('C',1999)
c_plus=Book('C++',1499)
generic_java=Book('GENERIC JAVA',599)
books=[python,scala,java,c,c_plus,generic_java]

author1=Author('Guido Van Rossum',64,'Dutch','PYTHON')
author2=Author('Martin Odersky',61,'German','SCALA')
author3=Author('James Gosling',65,'Canadian','JAVA')
author4=Author('Dennis Ritchie',79,'American','C')
author5=Author('Bjarne Stroustrup',69,'Danish','C++')
author6=Author('Martin Odersky',61,'German','GENERIC JAVA')
authors=[author1,author2,author3,author4,author5,author6]

books_by_author=input("Enter the Author Name to know about the number of books written by them: ")
print('\n*',books_by_author,"has written",no_of_books(authors,books_by_author),"books")

print("\n* The Price of all the books in the Store: ",total_price(books),'\n')

affortable_books(authors,books)
