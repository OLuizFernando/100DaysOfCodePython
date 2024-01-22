import csv

with open('dados_pessoas.csv') as arquivo:
    ficha = csv.reader(arquivo)
    idades = []
    for linha in ficha:
        if linha[1].isnumeric():
            idades.append(int(linha[1]))

print(idades)