
import keyboard
import os 

print (type(library))


library = {}
book_id = 1
library[book_id] ={
            "no" : book_id  , 
            "name": book_name,
            "author": book_author,
            "date": book_date ,
            "type": book_type , 
            "satat" : True 
    }
book_id += 1


while book_id >=0 :
    for value in library:
        print (library.values)
    input ("press any key to cont......")
    os.system ("cls")
    book_id -=1

    # print("add book is done.\n")
    # print ("press any key to cont....")
    # print ("book updade")
    # print("\n📚 list of books :")
    # for id, book in library.items():
    #     print(f"\n📖 no: {id}")
    #     for value in book.items():
    #         print(f"{value}")