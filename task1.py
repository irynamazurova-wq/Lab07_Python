import datetime


class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=None):

        self.surname = surname

        self.first_name = first_name

        self.nickname = nickname

        date_parts = birth_date_str.split('-')

        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])

        self.birth_date = datetime.date(year, month, day)

    def get_fullname(self):

        return self.surname + " " + self.first_name

    def get_age(self):

        today = datetime.date.today()


        age = today.year - self.birth_date.year

        if (today.month < self.birth_date.month) or \
                (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age = age - 1

        return str(age)


person1 = Person("Коваленко", "Олег", "2001-05-20", nickname="Колєга")

person2 = Person("Мельник", "Ірина", "2004-12-01", nickname="Манікюр")

person3 = Person("Собко", "Олег", "2004-12-18", nickname="СТО")

person4 = Person("Безпалюк", "Максим", "2005-06-11", nickname="Однокласник")

print("+1 Контакт")
print("Повне ім'я:", person1.get_fullname())
print("Дата народження (об'єкт):", person1.birth_date)
print("Вік:", person1.get_age())
print("Псевдонім:", person1.nickname)

print("+2 Контакт")
print("Повне ім'я:", person2.get_fullname())
print("Вік:", person2.get_age())
print("Псевдонім:", person2.nickname)

print("+3 Контакт")
print("Повне ім'я:", person3.get_fullname())
print("Дата народження (об'єкт):", person3.birth_date)
print("Вік:", person3.get_age())
print("Псевдонім:", person3.nickname)

print("+4 Контакт")
print("Повне ім'я:", person4.get_fullname())
print("Дата народження (об'єкт):", person4.birth_date)
print("Вік:", person4.get_age())
print("Псевдонім:", person4.nickname)