class Patient:
    def __init__(self, fn, mn, ln, address, city, state, zip_code, phone, \
                 emergency_contact_name, emergency_contact_phone):
        self.__first_name = fn
        self.__middle_name = mn
        self.__last_name = ln
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self._state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone(self):
        return self.__phone

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

    def set_first_name(self, fn):
        self.__first_name = fn

    def set_middle_name(self, mn):
        self.__middle_name = mn

    def set_last_name(self, ln):
        self.__last_name = ln

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone(self, phone):
        self._phone = phone

    def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone

    def __str__(self):
        return "First Name: " + self.__first_name + \
               "\nMiddle Name: " + self.__middle_name + \
               "\nLast Name: " + self.__last_name + \
               "\nAddress: " + self.__address + \
               "\nCity: " + self.__city + \
               "\nState: " + self.__state + \
               "\nZip Code: " + self.__zip_code + \
               "\nPhone: " + self.__phone + \
               "\nEmergency Contact Name: " + self.__emergency_contact_name + \
               "\nEmergency Contact Phone: " + self.__emergency_contact_phone + "\n"








