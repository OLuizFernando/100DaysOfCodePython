import pandas

ficha_dicio = {
    'livros': ['1984', 'A Metamorfose', 'Maus'],
    'autores': ['George Orwell', 'Franz Kafka', 'Art Spiegelman'],
    'ano': [1949, 1915, 1986]
}

ficha = pandas.DataFrame(ficha_dicio)
print(ficha)