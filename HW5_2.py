from colorama import Fore, Style


class Book:
    def __init__(self, title, author, publish_year, pages, language, price, status=None, read_pages=0, progress=0,
                 media_type="Book"):
        """
        description
        :param title: title of book
        :param author: author(s) of books
        :param publish_year: the year that the book published
        :param pages: number of pages
        :param language: language of book
        :param price: price of book
        :param status: status of book
        :param read_pages: Number of pages that read
        :param progress: percent of read pages
        :param media_type: type of media that equals to Book
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.status = status
        self.read_pages = read_pages
        self.progress = progress
        self.media_type = media_type

    def read(self):
        """
        get read pages from user
        :return: show the pages that user has already read and pages that left from book
        """
        new_read_pages = int(input(f"{Fore.LIGHTYELLOW_EX}"
                                   f"Please Enter number of pages that you read "
                                   f"from {self.title}: {Style.RESET_ALL}"))
        self.read_pages += new_read_pages

        if self.read_pages <= self.pages:
            print(f"{Fore.LIGHTCYAN_EX}you have read {self.read_pages} pages "
                  f"from {self.title}. "
                  f"There are {self.pages - self.read_pages} pages left... {Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}You can not read more than {self.pages} pages {Style.RESET_ALL}")

    def get_status(self):
        """
        :return: set the status of the book
        """
        if self.read_pages == 0:
            self.status = f"{Fore.YELLOW}Unread{Style.RESET_ALL}"
        elif self.read_pages < self.pages:
            self.status = f"{Fore.YELLOW}Reading{Style.RESET_ALL}"
        elif self.read_pages == self.pages:
            self.status = f"{Fore.YELLOW}Finished{Style.RESET_ALL}"
        else:
            print(f"{Fore.RED}you enter wrong number{Style.RESET_ALL}")

    def progress_percent(self):
        """
        :return: percent of pages of book that already have read
        """
        self.progress = round((self.read_pages / self.pages) * 100)
        print(f"{Fore.YELLOW}Progress : {self.progress} % {Style.RESET_ALL}")

    def __str__(self):
        """
        :return: information of book
        """
        print(f"{Fore.GREEN}title : {self.title} \n"
              f"author(s) : {self.author} \n"
              f"publish year : {self.publish_year} \n"
              f"pages : {self.pages} \n"
              f"language : {self.language} \n"
              f"price : {self.price} \n"
              f"status : {self.status} \n"
              f"progress : {self.progress}% {Style.RESET_ALL}")


class Magazine(Book):
    def __init__(self, title, author, publish_year, pages, language, price, issue, status=None, read_pages=0,
                 progress=0,media_type="Magazine"):
        """
        :param title: title of magazine
        :param author: author(s) of magazine
        :param publish_year: publish year of magazine
        :param pages: pages of magazine
        :param language: language of magazine
        :param price: price of magazine
        :param issue: issue of magazine
        :param status: status of magazine
        :param read_pages: read pages of magazine
        :param progress: percent of read pages from magazine
        :param media_type: media type that equal to magazine
        """
        super().__init__(title, author, publish_year, pages, language, price, status, read_pages, progress)
        self.issue = issue
        self.media_type = media_type

    def read(self):
        """
        get read pages from user
        :return: show the pages that user has already read and pages that left from magazine
        """
        super().read()

    def get_status(self):
        """
        :return: set the status of the magazine
        """
        super().get_status()

    def progress_percent(self):
        """
        :return: percent of pages of magazine that already have read
        """
        super(Magazine, self).progress_percent()

    def __str__(self):
        """
        :return: information of magazine
        """
        super().__str__()
        print(f"{Fore.GREEN}issue : {self.issue} \n"
              f"{Style.RESET_ALL}")


class PodcastEpisode(Book):
    def __init__(self, title, speaker, publish_year, time, language, price, listen_time=0, status=None, progress=0,
                 media_type="Podcast"):
        """
        :param title: title of Podcast
        :param speaker: speaker of Podcast
        :param publish_year: the year that the Podcast published
        :param time: time of Podcast
        :param language: language of Podcast
        :param price: price of Podcast
        :param status: status of Podcast
        :param listen_time: the time that user listened to Podcast
        :param progress: percent of listen time
        :param media_type: type of media that equals to Podcast
        """
        super().__init__(title, publish_year, language, price, status, progress)
        self.speaker = speaker
        self.time = time
        self.listen_time = listen_time
        self.media_type = media_type

    def listen(self):
        """
        get listen time from user
        :return: show the time that user has already listened and time that left from Podcast
        """
        new_listen_time = int(input(f"{Fore.LIGHTYELLOW_EX} Please Enter the time that you listen to "
                                    f"{self.title} : {Style.RESET_ALL}"))
        self.listen_time += new_listen_time

        if self.listen_time <= self.time:
            print(f"{Fore.LIGHTCYAN_EX}you have listen {self.listen_time} minutes "
                  f"from {self.title}. "
                  f"There are {self.time - self.listen_time} minutes left... {Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}You can not listen more than {self.time} minutes {Style.RESET_ALL}")

    def get_status(self):
        """
        :return: set the status of Podcast
        """
        if self.listen_time == 0:
            self.status = f"{Fore.YELLOW}Un listened{Style.RESET_ALL}"
        elif self.listen_time < self.pages:
            self.status = f"{Fore.YELLOW}listening{Style.RESET_ALL}"
        elif self.listen_time == self.pages:
            self.status = f"{Fore.YELLOW}Finished{Style.RESET_ALL}"
        else:
            print(f"{Fore.RED}you enter wrong number{Style.RESET_ALL}")

    def progress_percent(self):
        """
        :return: percent of time of Podcast that already have listened
        """
        self.progress = round((self.listen_time / self.time) * 100)
        print(f"{Fore.YELLOW}Progress : {self.progress} % {Style.RESET_ALL}")

    def __str__(self):
        super().__str__()
        print(f"{Fore.GREEN} Speaker : {self.speaker}\n"
              f"time : {self.time} \n"
              f"listen time : {self.listen_time}"
              f"{Style.RESET_ALL}")


class AudioBook(PodcastEpisode):
    def __init__(self, title, speaker, author, publish_year, pages, book_language, audio_language, time, price,
                 status=None, read_pages=0, listen_time=0, progress=0, media_type="AudioBook"):
        """
        :param title: title of AudioBook
        :param speaker: speaker of AudioBook
        :param author: author(s) of AudioBook
        :param publish_year: publish year of AudioBook
        :param pages: pages of AudioBook
        :param book_language: language of the book of AudioBook
        :param audio_language: language of audio
        :param time: time of AudioBook
        :param price: price of AudioBook
        :param status: status of AudioBook
        :param read_pages: read pages from AudioBook
        :param listen_time: listen time of AudioBook
        :param progress: progress percentage of AudioBook
        :param media_type: media type of AudioBook that equal to AudioBook
        """
        super().__init__(title, speaker, publish_year, time, book_language, price, listen_time, status, progress)
        self.author = author
        self.pages = pages
        self.read_pages = read_pages
        self.audio_language = audio_language
        self.media_type = media_type

    def listen(self):
        """
        get listen time from user
        :return: show the time that user has already listened and time that left from AudioBook
        """
        super().listen()

    def get_status(self):
        """
        :return: set the status of Podcast
        """
        super().get_status()

    def progress_percent(self):
        """
        :return: percent of time of AudioBook that already have listened
        """
        super(AudioBook, self).progress_percent()

    def __str__(self):
        """
        :return: information of AudioBook
        """
        super().__str__()
        print(f"{Fore.GREEN}"
              f"speaker : {self.speaker} \n"
              f"book language : {self.language} \n"
              f"audio language : {self.audio_language} \n"
              f"time : {self.time}"
              f"{Style.RESET_ALL}")


books_list = []
magazine_list = []
podcast_list = []
audio_list = []
bookshelf = []


def get_data_book():
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
    book = Book(title, author, publish_year, pages, language, price)
    books_list.append(book)
    bookshelf.append(book)


def get_data_magazine():
    """
    get data of magazine from user and make an instance of magazine class from user inputs and append magazines
     to magazines_list
    :return: do not return anything. just create a list of magazine Class instances
    """
    print(f"{Fore.LIGHTYELLOW_EX}--- Please fill the information of the magazine ---{Style.RESET_ALL}")
    title = input(f"{Fore.CYAN}Please enter title : ")
    author = input("Please enter author(s) : ")
    publish_year = input("Please enter publish year : ")
    pages = int(input("Please enter number of pages : "))
    language = input("Please enter language : ")
    price = input(f"Please enter price : ")
    issue = input(f"Please enter issue : {Style.RESET_ALL}")
    print("\n")
    magazine = Magazine(title, author, publish_year, pages, language, price, issue)
    magazine_list.append(magazine)
    bookshelf.append(magazine)


def get_data_podcast():
    """
    get data of podcast episode from user and make an instance of PodcastEpisode class from user inputs
    and append podcasts to podcasts_list
    :return: do not return anything. just create a list of PodcastEpisode Class instances
    """
    print(f"{Fore.LIGHTYELLOW_EX}--- Please fill the information of the podcast ---{Style.RESET_ALL}")
    title = input(f"{Fore.CYAN}Please enter title : ")
    speaker = input("Please enter speaker : ")
    publish_year = input("Please enter publish year : ")
    time = int(input("Please enter time : "))
    language = input("Please enter language : ")
    price = input(f"Please enter price : {Style.RESET_ALL}")
    print("\n")
    podcast = PodcastEpisode(title, speaker, publish_year, time, language, price)
    podcast_list.append(podcast)
    bookshelf.append(podcast)


def get_data_audio():
    """
    get data of audio book from user and make an instance of AudioBook class from user inputs
    and append audio books to audio_list
    :return: do not return anything. just create a list of AudioBook Class instances
    """
    print(f"{Fore.LIGHTYELLOW_EX}--- Please fill the information of the audio book ---{Style.RESET_ALL}")
    title = input(f"{Fore.CYAN}Please enter title : ")
    speaker = input("Please enter speaker : ")
    author = input("Please enter author(s) : ")
    publish_year = input("Please enter publish year : ")
    pages = int(input("Please enter number of pages : "))
    book_language = input("Please enter book language : ")
    audio_language = input("Please enter audio language : ")
    price = input(f"Please enter price : ")
    time = int(input(f"Please enter time : {Style.RESET_ALL}"))
    print("\n")
    audio = AudioBook(title, speaker, author, publish_year, pages, book_language, audio_language, time, price)
    audio_list.append(audio)
    bookshelf.append(audio)


def sort(lst, metric, reverse):
    """
    :param lst: list that we want to sort
    :param metric: the metric that we want to sort base on that
    :param reverse: sort descending (reverse = True) or Ascending (reverse = False)
    :return:
    """
    sorted_list = sorted(lst, key=lambda x: x.__getattribute__(metric), reverse=reverse)

    for _ in sorted_list:
        print(f"{Fore.YELLOW}media type: {_.media_type} \n"
              f"name : {_.title} \n"
              f"progress : {_.progress} %{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}---------------------------------------------{Style.RESET_ALL}")


print(f"{Fore.CYAN}---...---...---...---...---...---...---...---...---...---...---...---...---...---...---...---...")
print("---...---...---...---...---...---...--- Hello to You! ---...---...---...---...---...---...---...")
print(
    f"---...---...---...---...---...---...---...---...---...---...---...---...---...---...---...---...{Style.RESET_ALL}")

while True:
    """
    show the list and show the output that user want base on that list until user enter 6
    """
    print("What do you want to do?")
    print(f"{Fore.LIGHTCYAN_EX}1- Add Book/Magazine/PodcastEpisode/AudioBook")
    print("2- Show my bookshelf")
    print("3- Add read page or listen time")
    print("4- Show me the progress")
    print("5- Sort my bookshelf")
    print(f"6- Exit{Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}--- Please select one of the above items ---{Style.RESET_ALL}")

    num_input = int(input())

    if num_input == 1:
        # Add Book/Magazine/PodcastEpisode/AudioBook
        print(f"{Fore.LIGHTRED_EX}Which one would you like to add?{Style.RESET_ALL}")
        print("1- Book")
        print("2- Magazine")
        print("3- PodcastEpisode")
        print("4- AudioBook")

        add_num = int(input())

        if add_num == 1:
            # add book
            get_data_book()
            pass
        elif add_num == 2:
            # add Magazine
            get_data_magazine()
            pass
        elif add_num == 3:
            # add podcastEpisode
            get_data_podcast()
            pass
        elif add_num == 4:
            # add AudioBook
            get_data_audio()

        else:
            print(f"{Fore.LIGHTRED_EX}You enter a wrong number. please try later...{Style.RESET_ALL}")

    elif num_input == 2:
        # call str of each Class

        print(f"{Fore.LIGHTBLUE_EX}** Your Books **{Style.RESET_ALL}")
        for book in books_list:
            book.__str__()
        print("\n")

        print(f"{Fore.LIGHTBLUE_EX}** Your Magazines **{Style.RESET_ALL}")
        for magazine in magazine_list:
            magazine.__str__()
        print("\n")

        print(f"{Fore.LIGHTBLUE_EX}** Your Podcast Episodes **{Style.RESET_ALL}")
        for podcast in podcast_list:
            podcast.__str__()
        print("\n")

        print(f"{Fore.LIGHTBLUE_EX}** Your Audio Books **{Style.RESET_ALL}")
        for audio in audio_list:
            audio.__str__()
        print("\n")

    elif num_input == 3:
        # Add read page or listen time
        if len(bookshelf) == 0:
            print(f"{Fore.LIGHTRED_EX}please Add first ...{Style.RESET_ALL}")
            print("\n")
        else:
            print(f"{Fore.LIGHTRED_EX}witch one?{Style.RESET_ALL}")
            for i in range(len(bookshelf)):
                print(f"{i + 1}- {bookshelf[i].title}")
            shelf_input = int(input())
            if isinstance(bookshelf[shelf_input - 1], PodcastEpisode) or isinstance(bookshelf[shelf_input - 1],
                                                                                    AudioBook):
                bookshelf[shelf_input - 1].listen()
            else:
                bookshelf[shelf_input - 1].read()
            print("\n")

    elif num_input == 4:
        # Show me the progress
        if len(bookshelf) == 0:
            print(f"{Fore.LIGHTRED_EX}please Add first ...{Style.RESET_ALL}")
            print("\n")
        else:
            print(f"{Fore.LIGHTRED_EX}witch one?{Style.RESET_ALL}")
            for i in range(len(bookshelf)):
                print(f"{i + 1}- {bookshelf[i].title}")
            shelf_input = int(input())
            bookshelf[shelf_input - 1].progress_percent()
            print("\n")

    elif num_input == 5:
        # sort my bookshelf
        sort(bookshelf, "progress", True)
        print("\n")

    elif num_input == 6:
        # Exit
        print(f"{Fore.RED}*** Have a nice Day ***{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}you enter a wrong number. please try again!{Style.RESET_ALL}")
