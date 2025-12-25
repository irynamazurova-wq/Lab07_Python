import datetime
import csv

class Person:
    def __init__(self, surname, first_name, birth_date_str, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        parts = birth_date_str.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        self.birth_date = datetime.date(year, month, day)

    def get_fullname(self):
        return self.surname + " " + self.first_name

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month < self.birth_date.month) or \
                (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return str(age)


def modifier(filename):

    print(f"Обробка файлу: {filename}...")

    processed_data = []

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            person = Person(
                surname=row['surname'],
                first_name=row['first_name'],
                birth_date_str=row['birth_date'],
                nickname=row['nickname']
            )

            row['fullname'] = person.get_fullname()
            row['age'] = person.get_age()

            processed_data.append(row)

    new_filename = "modified_" + filename

    fieldnames = ['surname', 'first_name', 'fullname', 'nickname', 'birth_date', 'age']

    with open(new_filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(processed_data)

    print(f"Готово! Результат збережено у файл: {new_filename}")

modifier("contacts.csv")