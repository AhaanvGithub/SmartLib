# Libraries & DS
import csv
from node import Book

# Open CSV & Clean
listed_data = []
book_list = []

filename = "books_db.csv"
with open(filename, 'r', newline='', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        listed_data += [row]

# Gather extra data about dataset
genres = []
authors = []
recommenders = []
for i in range(1, len(listed_data)):
    category = Book(listed_data[i]).data_val["category"]
    writer = Book(listed_data[i]).data_val["author"]
    recommender = Book(listed_data[i]).data_val["recommender"]
    smthn = recommender.split("|")

    for x in range(len(smthn)):
        if smthn[x] not in recommenders:
            recommenders += [smthn[x]]

    if category not in genres:
        genres.append(category)

    if writer not in authors:
        authors.append(writer)

authors.sort()
genres.sort()
recommenders.sort()


# Functions for console application
def introduce():
    name = input("What's your name?\n")
    print(f"Hello {name}! Thank you for using SmartLibs, we will recommend you a book based on your: ")
    print("""    - Genre of choice
    - Recommender of choice
    - Pages of choice
    - Author of choice\n""")

    decided = decision()

    if decided == "g":
        return genre_of_choice()
    elif decided == "r":
        return recommender_of_choice()
    elif decided == "p":
        return pages_of_choice()
    elif decided == "a":
        return author_of_choice()
    else:
        return "Error"


def goodbye():
    print("Thank you for using SmartLibs!")


def decision():
    decided = input("""What would you like to choose?
('g' for genre, 'r' for recommender, 'p' for pages, 'a' for author, or 'b' to leave)
""")
    while decided not in ['g', 'r', 'p', 'a', 'b']:
        print("Oops, that doesn't seem like a valid input, please try again.")
        return decision()

    if decided == 'b':
        goodbye()

    if decided == "g":
        return genre_of_choice()
    elif decided == "r":
        return recommender_of_choice()
    elif decided == "p":
        return pages_of_choice()
    elif decided == "a":
        return author_of_choice()
    else:
        return "Error"


def yn(question, yes, no):
    user_response = input(question)
    if user_response == "y":
        yes()
    elif user_response == "n":
        no()
    else:
        print("Oops, that wasn't a valid option, lets try this again...")
        return yn(question, yes, no)


def take_back_to_main_menu():
    print("Taking you back to the main menu...")
    return decision()


def genre_of_choice():
    user_genre = input(
        "What genre would you like to view? Type 'op' to see the list of available genres, 'b' to go back, "
        "or type your genre:\n")
    if user_genre == 'op':
        print("Genres:")
        for j in genres:
            print("-", j)
        return genre_of_choice()
    elif user_genre == 'b':
        return take_back_to_main_menu()
    elif user_genre in genres:
        print("Here are the books in this section...")
        for a in range(1, len(listed_data)):
            current_book = Book(listed_data[a])
            if current_book.data_val["category"] == user_genre:
                current_book.get_book_data()
        print("")
        yn("Would you like to see another genre? Type y/n to continue:\n", genre_of_choice, take_back_to_main_menu)
    else:
        print("Oops, that doesn't seem like a valid genre, lets try this again...")
        return genre_of_choice()


def author_of_choice():
    user_author = input(
        "What author would you like to view from? Type 'op' to see the list of available authors, 'b' to go back, "
        "or the author:\n"
    )

    if user_author == 'op':
        print("Authors:")
        for y in authors:
            print("-", y)
        print("")
        return author_of_choice()
    elif user_author == "b":
        return take_back_to_main_menu()
    elif user_author.lower() in [i.lower() for i in authors]:
        print("Here are the listed books this author has written...")
        for w in range(1, len(listed_data)):
            current_book = Book(listed_data[w])
            if current_book.data_val["author"].lower() == user_author.lower() or \
                    current_book.data_val["author"].upper() == user_author.upper() or \
                    current_book.data_val["author"] == user_author:
                current_book.get_book_data()
        print("")
        yn("Would you like to see another authors book? Type y/n to continue:\n", author_of_choice,
           take_back_to_main_menu)
    else:
        print("Uh-oh, that command doesn't seem valid, let's try this again...")
        return author_of_choice()


def recommender_of_choice():
    user_recommend = input(
        "What recommender would you like to choose? Type 'op' to see the list of available recommenders, 'b' to go back"
        ", or type your recommender:\n")

    if user_recommend == 'op':
        print("Recommenders to select from:")
        for i in recommenders:
            print("-", i)
        print("")
        return recommender_of_choice()
    elif user_recommend == 'b':
        return take_back_to_main_menu()
    elif user_recommend.lower() in [i.lower() for i in recommenders]:
        for book in range(1, len(listed_data)):
            current_book = Book(listed_data[book])
            if user_recommend.lower() in current_book.data_val["recommender"].lower():
                current_book.get_book_data()
        print("")
        yn("Would you like to see books from another recommender? Type y/n to continue:\n", recommender_of_choice,
           take_back_to_main_menu)
    else:
        print("Oops, that doesn't seem like a valid command, lets try this again...")
        return recommender_of_choice()


def pages_of_choice():
    pass


introduce()
