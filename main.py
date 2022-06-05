import random
import json
import configparser
from faker import Faker


#Получение модели
def get_model():
    config = configparser.ConfigParser()
    config.read("conf.py")
    model_ = config["Model"]["model"]
    return model_

#Функция-генератор
def pk_gen(pk=1):
    pk += 1
    return pk

def decorator(take_title):
    def wrapper():
        result = "".join(take_title())
        try:
            if len(result) > 11:
                raise ValueError
        except ValueError:
            print("Title's len is too long")
        return result
    return wrapper

#Функция для получения названий книг
def take_title() -> str:
    file = open("books.txt", encoding="utf8")
    list_ = file.read().split("\n")[:-1]
    return list_[random.randint(0,4)]


# Функция для генерации случайного года
def random_year():
    year = random.randint(0, 2022)
    return year

# Функция для генерации случайного кол-ва страниц
def random_pages():
    pages = random.randint(1, 600)
    return pages

#Функция для генерации isbn13
def isbn_gen(i):
    Faker.seed(i)
    fake = Faker()
    return fake.isbn13()

# Функция для генерации случайного рейтинга
def random_rate(digits=2):
    rating = random.uniform(0, 5)
    return f"{rating:.{digits}f}"

# Функция для генерации случайной цены
def random_price(digits=2):
    price = random.random() * 1000
    return f"{price:.{digits}f}"

#Функция генерации автора
def author_gen(i):
    list_of_authors = []
    Faker.seed(i*random.randint(10,1000))
    fake = Faker('ru_RU')
    for _ in range(random.randint(1,3)):
        list_of_authors.append(fake.name())
    return list_of_authors

take_title = decorator(take_title)

def main():
    list_of_dict = []
    for i in range(100):
        list_of_dict.append({
        'model': get_model(),
        'pk': pk_gen(i),
        'fields': {
            'Title': take_title(),
            'year': random_year(),
            'pages': random_pages(),
            'isbn13': isbn_gen(i),
            'rating': random_rate(),
            'price': random_price(),
            'authors': author_gen(i),
            },
        })
    jsonString = json.dumps(list_of_dict, indent=3, ensure_ascii=False).encode('utf8')
    jsonFile = open("data.json", "wb")
    jsonFile.write(jsonString)
    jsonFile.close()
    return jsonFile


if __name__ == "__main__":
    main()
