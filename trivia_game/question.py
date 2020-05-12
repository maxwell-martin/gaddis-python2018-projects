class Question:
    def __init__(self, question, one, two, three, four, answer):
        self.__question = question
        self.__one = one
        self.__two = two
        self.__three = three
        self.__four = four
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_one(self):
        return self.__one

    def get_two(self):
        return self.__two

    def get_three(self):
        return self.__three

    def get_four(self):
        return self.__four

    def get_answer(self):
        return self.__answer

    def set_question(self, question):
        self.__question = question

    def set_one(self, one):
        self.__one = one

    def set_two(self, two):
        self.__two = two

    def set_three(self, three):
        self.__three = three

    def set_four(self, four):
        self.__four = four

    def set_answer(self, answer):
        self.__answer = answer
