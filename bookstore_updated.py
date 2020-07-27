class Book:
    def __init__(self,name,price,author):
        self.name=name
        self.price=price
        self.author=author


    def affortable_books(books):
        affort_books=[]
        for i in books:       
            if i.price<1000:
                affort_books.append(i.name)
        for i in books:
            for j in affort_books:
                if i.name==j:
                    print("\n* The book '",j,"' written by '",i.author,"' is in affortable price")
    
         
class Author:
    def __init__(self,name,age,nationality):
        self.name=name
        self.age=age
        self.nation=nationality

                

def total_price(books):
    total_cost=0
    for i in books:
        total_cost=total_cost+i.price
    return total_cost    

def no_of_books(books,book_by_author):
    count=0
    for i in books:
        if(book_by_author.lower()==i.author.lower()):
            count=count+1
    return count       
        


python=Book('PYTHON',999,'Guido Van Rossum')
scala=Book('SCALA',1500,'Martin Odersky')
java=Book('JAVA',800,'James Gosling')
c=Book('C',1999,'Dennis Ritchie')
c_plus=Book('C++',1499,'Bjarne Stroustrup')
generic_java=Book('GENERIC JAVA',599,'Martin Odersky')
books=[python,scala,java,c,c_plus,generic_java]

author1=Author('Guido Van Rossum',64,'Dutch')
author2=Author('Martin Odersky',61,'German')
author3=Author('James Gosling',65,'Canadian')
author4=Author('Dennis Ritchie',79,'American')
author5=Author('Bjarne Stroustrup',69,'Danish')
author6=Author('Martin Odersky',61,'German')
authors=[author1,author2,author3,author4,author5,author6]


books_by_author=input("Enter the Author Name to know about the number of books written by them: ")
print('\n',books_by_author,'has written',no_of_books(books,books_by_author),'books')

print("\n* The Price of all the books in the Store: ",total_price(books))
Book.affortable_books(books)

#output

'''
Enter the Author Name to know about the number of books written by them: james gosling

 james gosling has written 1 books

* The Price of all the books in the Store:  7396

* The book ' PYTHON ' written by ' Guido Van Rossum ' is in affortable price

* The book ' JAVA ' written by ' James Gosling ' is in affortable price

* The book ' GENERIC JAVA ' written by ' Martin Odersky ' is in affortable price

'''
