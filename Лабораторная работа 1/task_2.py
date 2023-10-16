# TODO Найдите количество книг, которое можно разместить на дискете

pages = 100
lines = 50
symbols = 25
disk = (1024 ** 2) * 1.44
books = disk // (pages * lines * symbols * 4)
books = round(books)

print("Количество книг, помещающихся на дискету:", books)
