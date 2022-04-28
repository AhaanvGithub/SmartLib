# Libraries & DS
import csv
import time

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
    each_recommender = recommender.split("|")

    for x in range(len(each_recommender)):
        if each_recommender[x] not in recommenders:
            recommenders += [each_recommender[x]]

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
    time.sleep(3)


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
        print(f"Here are the books in the genre {user_genre.title()}...")
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
        print(f"Here are the listed books {user_author.title()} has written...")
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
        print(f"Here are books recommended by {user_recommend.title()}:")
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
    user_choose_option = input("Would you like a specific amount of pages or a range of pages? Type 's' for a "
                               "specific number of pages and 'r' for a range of pages, or 'b' to go back:\n")
    if user_choose_option == "s":
        return pages_specific()
    elif user_choose_option == "r":
        return pages_range()
    elif user_choose_option == "b":
        return take_back_to_main_menu()
    else:
        print("Uh-oh, that doesn't seem like a valid choice, lets try this again...")
        return pages_of_choice()


def pages_specific():
    user_specific = input("How many pages do you want your book to have exactly? Type your number of pages below, "
                          "or type 'b' to go back:\n")
    if user_specific == 'b':
        return pages_of_choice()
    elif user_specific.isdigit():
        list_of_valid_books = []
        for index in range(1, len(listed_data)):
            current_book = Book(listed_data[index])
            if current_book.data_val["pages"] == user_specific:
                list_of_valid_books.append(current_book)

        if len(list_of_valid_books) == 0:
            print("Uh-oh, this number of pages doesn't see, to be available...")
        else:
            print(f"Here are the books that have {user_specific} pages:")
            for i in list_of_valid_books:
                i.get_book_data()
            print("")
        yn("Would you like to try searching for more books again? Type y/n to continue:\n", pages_of_choice,
           take_back_to_main_menu)
    else:
        print("Oops, that doesn't seem like an integer or command, lets try this again...")
        return pages_specific()


def pages_range():
    user_range_minimum = input("What is the minimum number of pages you're looking for? (type 'b' to leave)\n")
    if user_range_minimum == 'b':
        return take_back_to_main_menu()
    while not user_range_minimum.isdigit():
        print("Uh-oh, that doesn't seem like a number we can search for, lets try this again...")
        user_range_minimum = input("What is the minimum number of pages you're looking for? (type 'b' to leave)\n")
        if user_range_minimum == 'b':
            return take_back_to_main_menu()

    user_range_maximum = input("What is the maximum number of pages you're looking for? (type 'b' to leave)\n")
    if user_range_maximum == 'b':
        return take_back_to_main_menu()
    while not user_range_maximum.isdigit():
        print("Uh-oh, that doesn't seem like a number we can search for, lets try this again...")
        user_range_maximum = input("What is the maximum number of pages you're looking for? (type 'b' to leave)\n")
        if user_range_maximum == 'b':
            return take_back_to_main_menu()

    if int(user_range_minimum) > int(user_range_maximum):
        print("Uh-oh! It seems like your minimum number of pages ({0}) is greater than your maximum number of pages "
              "({1}), let's try this again...".format(user_range_minimum, user_range_maximum))
        pages_range()
    elif user_range_minimum == user_range_maximum:
        print("It seems your minimum number of pages ({0}) is the exact same as your maximum number of pages ({1}), "
              "this will require a specific amount of pages...".format(user_range_minimum, user_range_maximum))
        pages_specific()
    else:
        available_books = []
        for i in range(1, len(listed_data)):
            current_book = Book(listed_data[i])
            if current_book.data_val["pages"] == "":
                continue
            if int(user_range_minimum) < int(current_book.data_val["pages"]) < int(user_range_maximum):
                available_books.append(current_book)

        if len(available_books) > 0:
            for i in available_books:
                i.get_book_data()
            print("")
            yn("Would you like to search for more books page-specific? Type y/n to continue:\n", pages_of_choice,
               take_back_to_main_menu)
        else:
            yn("Uh-oh! There doesn't seem to be any books available in this range, would you like to try again? "
               "Type y/n to continue:\n", pages_range, take_back_to_main_menu)


introduce()
