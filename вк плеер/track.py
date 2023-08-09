class Track:
    __author = str
    __name = str
    __url = str

    def __init__(self, author: str, name: str, url: str):

        """
        Это конструктор класса Track
        :param author: автор трека
        :param name: название трека
        :param url: ссылка на VK Music
        """
        self.__author = author
        self.__name = name
        self.__url = url

    @property
    def author(self):
        """
        Эта функция возвращает автора трека,
        :return: возвращает автора трека
        """

        return self.__author

    @property
    def name(self):
        """
        Эта функция возвращает название трека,
        :return: возвращает название трека
        """

        return self.__name

    @property
    def url(self):
        """
        Эта функция возвращает url трека,
        :return: возвращает url трека
        """

        return self.__url
