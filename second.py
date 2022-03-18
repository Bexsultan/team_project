spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

set_1 = set(spisok_1)
set_2 = set(spisok_2)

set_2.difference(set_1)
print(set_2)
