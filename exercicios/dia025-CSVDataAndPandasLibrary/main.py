import csv

with open('dados_pessoas.csv') as arquivo:
    ficha = csv.reader(arquivo)
    for linha in ficha:
        print(linha)