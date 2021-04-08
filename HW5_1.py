from colorama import Fore, Back, Style
# from termcolor import colored


class Books:
    def __init__(self, title, author, publish_year, pages, language,
                 price, get_status=f"{Fore.YELLOW}unread{Style.RESET_ALL}", read_pages=0):
        """
        description
        :param title: title of book
        :param author: author(s) of books
        :param publish_year: the year that the book published
        :param pages: number of pages
        :param language: language of book
        :param price: price of book
        :param get_status: status of book
        :param read_pages: number of read pages of book
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.get_status = get_status
        self.read_pages = read_pages

    def read(self):
        """
        get input of read pages of a book
        :return: print number of read pages and number of pages that left
        AND
        :return: status of a book
        update read pages
        """
        new_read_pages = int(input(f"{Fore.LIGHTYELLOW_EX}Please Enter number of pages that you read "
                                   f"from {self.title}: {Style.RESET_ALL}"))
        self.read_pages += new_read_pages

        if self.read_pages <= self.pages:
            print(f"{Fore.LIGHTCYAN_EX}you have read {self.read_pages} pages "
                  f"from {self.title}. "
                  f"There are {self.pages - self.read_pages} pages left... {Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}You can not read more than {self.pages} pages {Style.RESET_ALL}")

        if self.read_pages == 0:
            self.get_status = f"{Fore.YELLOW}Unread{Style.RESET_ALL}"
        elif self.read_pages < self.pages:
            self.get_status = f"{Fore.YELLOW}Reading{Style.RESET_ALL}"
        elif self.read_pages == self.pages:
            self.get_status = f"{Fore.YELLOW}Finished{Style.RESET_ALL}"
        else:
            print(f"{Fore.RED}you enter wrong number{Style.RESET_ALL}")

    def __str__(self):
        """
        :return: information of book
        """
        print(f"{Fore.GREEN}title : {self.title} \n"
              f"author(s) : {self.author} \n"
              f"publish year : {self.publish_year} \n"
              f"pages : {self.pages} \n"
              f"language : {self.language} \n"
              f"price : {self.price}"
              f"status : {self.get_status}"
              f"read pages: {self.read_pages} {Style.RESET_ALL}")


books_list = []


def get_data():
    """
    get data of book from user and make an instance of Books class from user inputs and append the book to books_list
    :return: do not return anything. just create a list of Books Class instances
    """
    print(f"{Fore.LIGHTYELLOW_EX}--- Please fill the information of the book ---{Style.RESET_ALL}")
    title = input(f"{Fore.CYAN}Please enter title : ")
    author = input("Please enter author(s) : ")
    publish_year = input("Please enter publish year : ")
    pages = int(input("Please enter number of pages : "))
    language = input("Please enter language : ")
    price = input(f"Please enter price : {Style.RESET_ALL}")
    print("\n")
    book = Books(title, author, publish_year, pages, language, price)
    books_list.append(book)


while True:
    """
    This while get input from user and base on those inputs, call functions of class for her/him until user wants to Exit
    """
    print("What do you do ? ")
    print(f"{Fore.BLUE}1 - Add a Book")
    print("2 - Add read pages")
    print("3 - Print all books")
    print("4 - Get status")
    print(f"5 - Exit{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}--- Please select one of the above items ---{Style.RESET_ALL}")

    num_input = int(input())

    if num_input == 1:
        get_data()

    elif num_input == 2:
        if len(books_list) > 1:
            print(f"{Fore.LIGHTRED_EX}Which one ?{Style.RESET_ALL}")
            for i in range(len(books_list)):
                print(f"{i + 1}- {books_list[i].title} ({books_list[i].pages} page)")
            chosen_book = input()
            if "," in chosen_book:
                chosen = chosen_book.split(",")
                for i in chosen:
                    books_list[int(i) - 1].read()
            else:
                books_list[int(chosen_book) - 1].read()
            print("\n")
        elif len(books_list) == 1:
            books_list[0].read()
            print("\n")
        else:
            print(f"{Fore.RED}Something were Wrong ... please select again!{Style.RESET_ALL}")

    elif num_input == 3:
        for i in range(len(books_list)):
            print(f"{Fore.LIGHTBLUE_EX}'{books_list[i].title}' book information: {Style.RESET_ALL}")
            books_list[i].__str__()
            print("\n")

    elif num_input == 4:
        if len(books_list) > 1:
            print(f"{Fore.LIGHTRED_EX}Which one ?{Style.RESET_ALL}")
            for i in range(len(books_list)):
                print(f"{i + 1}- {books_list[i].title}")
            chosen_book = int(input())
            print(f"{Fore.LIGHTBLUE_EX}status of {books_list[chosen_book - 1].title} is {books_list[chosen_book - 1].get_status} {Style.RESET_ALL}")
            print("\n")
        elif len(books_list) == 1:
            print(f"{Fore.LIGHTBLUE_EX}status of {books_list[0].title} is {books_list[0].get_status} {Style.RESET_ALL}")
            print("\n")

    elif num_input == 5:
        print(f"{Fore.LIGHTRED_EX}---Thanks---{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.LIGHTRED_EX}Something were Wrong ... please select again!{Style.RESET_ALL}")
        break

