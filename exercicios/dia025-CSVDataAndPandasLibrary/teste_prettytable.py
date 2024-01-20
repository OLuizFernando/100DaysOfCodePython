from prettytable import PrettyTable

with open('dados_pessoas.csv', mode='r', encoding='utf-8') as arquivo:
    ficha = arquivo.read().replace('\n', ',').split(',')

t = PrettyTable()
t.field_names = ficha[0:3]
for i in range(3, len(ficha), 3):
    t.add_row(ficha[i:i+3])

t.sortby = 'Idade'
print(t)