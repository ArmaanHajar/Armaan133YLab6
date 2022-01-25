from Database import Database

class Name:
    __year = 0
    __gender = ""
    __name_count = 0
    __name = ""

    def __init__(self, name_count, name, year, gender):
        self.__name_count = name_count
        self.__name = name
        self.__year = year
        self.__gender = gender

    # getters

    def get_name_count(self):
        return self.__name_count

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_gender(self):
        return self.__gender

    @staticmethod
    def fetch_names(year, gender):
        return Database.fetch_names(year, gender)